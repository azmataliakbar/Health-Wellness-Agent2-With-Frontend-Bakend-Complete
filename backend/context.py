from typing import Optional, List, Dict
from pydantic import BaseModel

class UserSessionContext(BaseModel):
    """
    Shared context class for tracking user session data across all tools and agents.
    Includes personal details, goals, plans, and interaction history.
    """
    name: str = "Anonymous"
    uid: int = 0
    goal: Optional[dict] = None
    diet_preferences: Optional[str] = None
    workout_plan: Optional[dict] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: List[str] = []
    progress_logs: List[Dict[str, str]] = []

    def update_progress(self, update: str):
        """Log progress updates with timestamp"""
        from datetime import datetime
        self.progress_logs.append({
            "timestamp": datetime.now().isoformat(),
            "update": update
        })

    def log_handoff(self, agent_name: str):
        """Record handoff events"""
        from datetime import datetime
        self.handoff_logs.append(f"{datetime.now().isoformat()} - Handoff to {agent_name}")