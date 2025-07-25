from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from main import HealthWellnessAgent, UserSessionContext
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv, find_dotenv
from typing import Optional
import logging
from pydantic import BaseModel

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def needs_openai_fallback(response: str) -> bool:
    """Check if we need OpenAI fallback"""
    return "__FALLBACK__" in response

# Initialize FastAPI
app = FastAPI(
    title="Health Assistant API",
    version="1.0",
    description="API for health queries with OpenAI fallback"
)

# Load environment
load_dotenv(find_dotenv())
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
agent = HealthWellnessAgent()
context = UserSessionContext()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryResponse(BaseModel):
    response: str
    source: str
    tokens_used: Optional[int] = None

@app.get("/")
async def health_check():
    return {
        "status": "running",
        "docs": "http://127.0.0.1:8000/docs"
    }

@app.post("/query", response_model=QueryResponse)
async def handle_query(user_input: str = Query(..., min_length=2, max_length=200)):
    try:
        # Try local response first
        local_response = await agent.handle_message(user_input, context)
        
        if not needs_openai_fallback(local_response):
            return {"response": local_response, "source": "local"}
            
        # Fallback to OpenAI
        ai_response = await client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": """You are a certified health assistant. Follow these rules:
            1. For factual queries: Provide concise 1-2 sentence answers
            2. For instructional content: Use bullet points
            3. For controversial topics: State "Consult your doctor"
            4. Never make medical diagnoses
            5. Format numbers clearly (e.g. "8-12 reps")
            6. Use metric units by default"""
        },
        {
            "role": "user",
            "content": user_input
        }
    ],
    max_tokens=120,  # Slightly increased for better formatting
    temperature=0.5,  # Balanced between creativity and accuracy
    top_p=0.9,
    frequency_penalty=0.2,  # Reduces repetition
    presence_penalty=0.1    # Encourages topic focus
)
        
        return {
            "response": ai_response.choices[0].message.content,
            "source": "openai",
            "tokens_used": ai_response.usage.completion_tokens
        }
        
    except Exception :
        logger.exception("🔴 Exception during OpenAI query processing")  # logs full traceback

    raise HTTPException(
        status_code=500,
        detail=(
            "❌ Something went wrong while processing your query.\n"
            "🔍 Possible causes:\n"
            "1. Missing or incorrect OPENAI_API_KEY in your .env file.\n"
            "2. Network or timeout issue connecting to OpenAI servers.\n"
            "3. Malformed or invalid request payload.\n"
            "4. OpenAI API limit or service outage.\n"
            "📋 Check server logs for full error trace."
        )
    )

if __name__ == "__main__":
    import uvicorn
    logger.info("\n🚀 Server starting...")
    logger.info("📚 API Docs: http://127.0.0.1:8000/docs")
    logger.info("⚡ Interactive: http://127.0.0.1:8000/redoc\n")
    
    # Corrected uvicorn.run() call
    uvicorn.run(
        "fast_api:app",  # Changed to import string format
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )