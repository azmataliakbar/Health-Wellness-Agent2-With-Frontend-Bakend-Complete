import asyncio
import os
import logging
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI
from agent import HealthWellnessAgent
from context import UserSessionContext

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Assistant:
    def __init__(self):
        self.client = None
        self.agent = HealthWellnessAgent()
        self.context = UserSessionContext()
        self.running = False
        self.token_count = 0  # Track token usage

    async def initialize_openai(self):
        """Initialize OpenAI client with token-efficient settings"""
        try:
            load_dotenv(find_dotenv())
            openai_key = os.getenv("OPENAI_API_KEY", "").strip()
            
            if not openai_key or not openai_key.startswith('sk-'):
                logger.warning("OpenAI disabled - missing/invalid key")
                return False

            self.client = AsyncOpenAI(
                api_key=openai_key,
                timeout=10.0
            )

            # Minimal connection test
            test = await self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "ping"}],
                max_tokens=5
            )
            self.token_count += test.usage.total_tokens
            logger.info(f"OpenAI ready | Test used {test.usage.total_tokens} tokens")
            return True

        except Exception as e:
            logger.error(f"OpenAI init failed: {str(e)}")
            return False

    async def get_response(self, user_input: str) -> str:
        """Get response with token-efficient fallback"""
        local_response = await self.agent.handle_message(user_input, self.context)
        
        if local_response.strip() != "__FALLBACK__":
            return local_response
            
        if not self.client:
            return "I need more information to answer that. [AI service unavailable]"

        try:
            logger.info("Using OpenAI fallback...")
            response = await self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "Answer extremely concisely (1 sentence max)."
                    },
                    {
                        "role": "user", 
                        "content": user_input
                    }
                ],
                temperature=0.3,  # More deterministic
                max_tokens=50,    # Strict limit
                top_p=0.5         # Reduce randomness
            )
            self.token_count += response.usage.total_tokens
            logger.info(f"Used {response.usage.total_tokens} tokens (Total: {self.token_count})")
            return response.choices[0].message.content
            
        except Exception as e:
            logger.error(f"OpenAI error: {str(e)}")
            return "I couldn't retrieve an answer. [Service error]"

    async def run(self):
        print("\n🌿 Health & Wellness Assistant 🌿")
        print("Type 'exit' or 'quit' to end session\n")
        
        if not await self.initialize_openai():
            print("Note: Advanced AI features disabled")

        self.running = True
        while self.running:
            try:
                user_input = (await asyncio.to_thread(input, "\n💬 You: ")).strip()
                
                if user_input.lower() in ("exit", "quit"):
                    self.running = False
                    continue
                    
                if not user_input:
                    continue
                
                response = await self.get_response(user_input)
                print(f"\n🤖 Assistant: {response}")
                
            except KeyboardInterrupt:
                print("\nEnding session...")
                self.running = False
                
        print(f"\nSession ended | Total tokens used: {self.token_count}")

if __name__ == "__main__":
    assistant = Assistant()
    try:
        asyncio.run(assistant.run())
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        print("\n⚠️  The assistant crashed. Please restart.")
