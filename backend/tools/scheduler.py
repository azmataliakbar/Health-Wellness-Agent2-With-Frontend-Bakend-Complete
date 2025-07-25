# health_wellness_agent2/tools/scheduler.py
from typing import Any
import asyncio
from context import UserSessionContext

async def schedule_checkin(context: UserSessionContext) -> str:
    """Enhanced Monday check-in response with tips and change option"""
    await asyncio.sleep(0)  # Maintains async compatibility
    
    return (
        "📅 Weekly Check-in Schedule\n\n"
        "⏰ Every Monday at 9 AM\n\n"
        "✨ What to track each week:\n"
        "• Body measurements 📏\n"
        "• Progress photos 📸\n"
        "• Workout completion ✅\n\n"

        "💡 Tips for best results:\n"
        "1. Take photos in consistent lighting\n"
        "2. Measure at the same time of day\n"
        "3. Wear similar clothing for photos\n"
        "4. Record notes about your week\n\n"
        
        "⚙️ Change with: /schedule weekly|biweekly|monthly\n\n"

        "🔔 Set a recurring phone reminder!"
    )