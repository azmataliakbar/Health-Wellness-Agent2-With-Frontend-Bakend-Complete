# health_wellness_agent2/agents/injury_support_agent.py
import asyncio
from context import UserSessionContext
from typing import Any

class InjurySupportAgent:
    """Specialized agent for injury-related fitness modifications"""
    
    def __init__(self):
        self.injury_modifications = {
            "knee": {
                "avoid": ["🏃 Any Type Of Running", "🤸 Any Type Of Jumping", "🪑 Deep squats", "🦵 Lunges"],
                "alternatives": ["🏊 Any Type Of Swimming", "💪 Any Type Of Upper body strength", "🪑 Chair exercises", "🧘 Gentle yoga"],
                "tips": ["❄️ Use ice after activity", "🔼 Elevate when resting", "🚫 Avoid high-impact activities"]
            },
            "back": {
                "avoid": ["🏋️ Heavy lifting", "🔄 Twisting motions", "💥 High-impact activities"],
                "alternatives": ["🚶 Any Type Of Walking", "🏊 Any Type Of Swimming", "🧘 Soft stretching", "🔄 Core strengthening"],
                "tips": ["🧍 Maintain good posture", "⬆️ Use proper lifting technique", "🛌 Sleep with pillow support"]
            },
            "shoulder": {
                "avoid": ["☝️ Overhead movements", "🏋️ Heavy pushing/pulling", "🤼 Contact sports"],
                "alternatives": ["🦵 Lower body exercises", "💪 Gentle arm movements", "🚶 Walking", "❤️ Light cardio"],
                "tips": ["❄️ Apply ice after activity", "🛌 Avoid sleeping on injured side", "🔄 Gentle range of motion"]
            },
            "ankle": {
                "avoid": ["🏃 Running", "🤸 Jumping", "⚽ High-impact sports", "🏞️ Uneven surfaces"],
                "alternatives": ["💪 Upper body strength", "🏊 Swimming", "🪑 Seated exercises", "🧘 Soft stretching"],
                "tips": ["❄️ Use RICE protocol", "👟 Wear supportive footwear", "🚫 Avoid uneven ground"]
            },
            "foot": {
                "avoid": ["🏃 Running", "🤸 Jumping", "⚽ High-impact sports", "🛣️ Long walks on hard surfaces"],
                "alternatives": ["💪 Upper body strength", "🏊 Swimming", "🪑 Seated exercises", "🧘 Gentle stretching"],
                "tips": ["❄️ Use RICE protocol", "👟 Wear supportive footwear", "🚫 Avoid uneven ground", "🦶 Consider arch support"]
            },
            "wrist": {
                "avoid": ["🏋️ Heavy lifting", "🖐️ Push-ups", "🤲 Weight-bearing on hands", "🔄 Repetitive motions"],
                "alternatives": ["🦵 Lower body exercises", "🏃 Cardio machines", "🧘 Gentle stretching", "🚶 Walking"],
                "tips": ["🩹 Use wrist supports", "❄️ Apply ice after activity", "🚫 Avoid repetitive gripping"]
            }
        }

    async def handle_message(self, message: str, context: UserSessionContext) -> str:
        """Process injury-related fitness concerns asynchronously"""
        # Simulate async database/API call
        await asyncio.sleep(0.1)  # Small delay to simulate async operation
        
        injury_type = self._identify_injury_type(message)
        
        if injury_type in self.injury_modifications:
            return await self._generate_injury_specific_advice(injury_type)
        
        return await self._generate_general_injury_advice()

    def _identify_injury_type(self, message: str) -> str:
        """Identify type of injury from message"""
        message_lower = message.lower()
        
        injury_keywords = {
            "knee": ["knee", "kneecap", "patella"],
            "back": ["back", "spine", "lower back", "upper back"],
            "shoulder": ["shoulder", "rotator cuff", "arm"],
            "ankle": ["ankle"],
            "foot": ["foot", "feet", "toe", "heel"],
            "wrist": ["wrist", "hand"]
        }
        
        for injury, keywords in injury_keywords.items():
            if any(word in message_lower for word in keywords):
                return injury
        
        return "unknown"

    async def _generate_injury_specific_advice(self, injury_type: str) -> str:
        """Generate advice for specific injury types asynchronously"""
        await asyncio.sleep(0.05)  # Simulate async processing
        info = self.injury_modifications[injury_type]
        
        return (
            f"🏥 **{injury_type.upper()} INJURY SUPPORT**\n\n"
            f"🚑 **Exercises to Avoid:**\n"
            f"{chr(10).join(info['avoid'])}\n\n"
            f"✅ **Safe Alternatives:**\n"
            f"{chr(10).join(info['alternatives'])}\n\n"
            f"💡 **Recovery Tips:**\n"
            f"{chr(10).join(info['tips'])}\n\n"
            f"🔄 **Recovery Phases:**\n"
            "1. Pain-free movement\n"
            "2. Gentle strengthening\n"
            "3. Functional exercises\n"
            "4. Return to activity\n\n"
            "⚠️ **Stop if pain occurs and consult a doctor for persistent pain**"
        )

    async def _generate_general_injury_advice(self) -> str:
        """Generate general injury advice asynchronously"""
        await asyncio.sleep(0.05)  # Simulate async processing
        return (
            "🩹 **GENERAL INJURY ADVICE**\n\n"
            "🛡️ **Safety First:**\n"
            "• Stop if pain occurs\n"
            "• Start with low-impact activities\n"
            "• Progress slowly\n\n"
            "🏊 **Recommended Activities:**\n"
            "• Swimming/water exercises\n"
            "• Stationary biking\n"
            "• Gentle walking\n"
            "• Chair exercises\n\n"
            "🍎 **Nutrition for Healing:**\n"
            "• Anti-inflammatory foods\n"
            "• Adequate protein\n"
            "• Stay hydrated\n\n"
            "🏥 **Consult a healthcare professional for proper diagnosis and treatment**"
        )
