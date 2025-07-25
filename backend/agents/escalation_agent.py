# health_wellness_agent2/agents/escalation_agent.py
import time
from context import UserSessionContext

class EscalationAgent:
    ESCALATION_KEYWORDS = [
        "human", "real trainer", "speak to someone",
        "human help", "live agent", "talk to person",
        "coach", "real person", "talk to someone"
    ]

    def should_escalate(self, input: str) -> bool:
        """Check if message contains escalation keywords"""
        input_lower = input.lower()
        return any(kw in input_lower for kw in self.ESCALATION_KEYWORDS)

    def generate_response(self, message: str, context: UserSessionContext) -> str:
        """Generate escalation response without requiring user_id"""
        ref_id = f"HC-{int(time.time())}"  # Simplified reference ID
        return (
            f"🔴 CONNECTING YOU TO HUMAN COACH 🔴\n\n"
            f"📝 Reference ID: {ref_id}\n"
            f"💬 Your Request: \"{message[:100]}\"\n\n"
            "⏳ Next Steps:\n"
            "1. Certified coach will contact you\n"
            "2. Prepare your fitness history\n\n"
            "📞 Immediate Assistance:\n"
            "• ☎️ 800-555-HELP\n"
            "• 📧 support@healthcoach.com"
        )