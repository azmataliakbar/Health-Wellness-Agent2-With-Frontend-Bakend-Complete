# health_wellness_agent2/agent.py

import asyncio
from typing import Optional
from context import UserSessionContext
from tools.goal_analyzer import analyze_goal
from tools.meal_planner import generate_meal_plan
from tools.workout_recommender import recommend_workout
from tools.scheduler import schedule_checkin
from tools.tracker import track_progress, log_activity, search_progress
from agents.escalation_agent import EscalationAgent
from agents.injury_support_agent import InjurySupportAgent
from agents.nutrition_expert_agent import NutritionExpertAgent

class HealthWellnessAgent:
    def __init__(self):
        self.tools = {
            "analyze_goal": analyze_goal,
            "generate_meal_plan": generate_meal_plan,
            "recommend_workout": recommend_workout,
            "schedule_checkin": schedule_checkin,
            "track_progress": track_progress,
            "log_activity": log_activity,
            "search_progress": search_progress
        }

        self.escalation_agent = EscalationAgent()
        self.injury_support_agent = InjurySupportAgent()
        self.nutrition_expert_agent = NutritionExpertAgent()

        self._init_command_handlers()
        self._init_handoff_triggers()

    def _init_command_handlers(self):
        """Initialize command to handler mappings"""
        self.command_handlers = [
            (["monday", "check-in", "remind", "schedule"], self._handle_schedule),
            (["track ", "log "], self._handle_tracking),
            (["progress", "stats", "how am i doing"], self._handle_progress),
            (["workout", "exercise", "train", "gym"], self._handle_workout),
            (["meal", "diet", "food", "nutrition"], self._handle_nutrition)
        ]

    def _init_handoff_triggers(self):
        """Initialize keywords that trigger handoff to specialized agents"""
        self.handoff_triggers = {
            "escalation": ["human", "coach", "real person", "talk to someone"],
            "injury": ["injury", "pain", "hurt", "recovery", "rehab"],
            "nutrition": ["diabetes", "blood pressure", "hypertension",
                        "allergy", "weight loss", "energy", "medical diet"]
        }

    def _check_handoff_triggers(self, input_lower: str) -> Optional[str]:
        """Check if input matches any handoff trigger keywords"""
        for agent_type, triggers in self.handoff_triggers.items():
            if any(trigger in input_lower for trigger in triggers):
                return agent_type
        return None

    async def _handle_agent_handoff(self, agent_type: str, input: str, context: UserSessionContext) -> str:
        """Route message to appropriate specialized agent"""
        if agent_type == "escalation":
            if self.escalation_agent.should_escalate(input):
                return self.escalation_agent.generate_response(input, context)
        elif agent_type == "injury":
            return await self.injury_support_agent.handle_message(input, context)
        elif agent_type == "nutrition":
            return await self.nutrition_expert_agent.handle_message(input, context)

        # fallback to default routing
        return await self._route_command(input.lower(), context)

    async def handle_message(self, input: str, context: Optional[UserSessionContext] = None) -> str:
        if context is None:
            context = UserSessionContext()

        try:
            input_lower = input.lower()

            # Check for handoff to specialized agents
            handoff_agent = self._check_handoff_triggers(input_lower)
            if handoff_agent:
                return await self._handle_agent_handoff(handoff_agent, input, context)

            # Then fallback to regular commands
            return await self._route_command(input_lower, context)

        except Exception as e:
            return self._format_error(e)

    async def _handle_nutrition_expert(self, input_lower: str, context: UserSessionContext) -> str:
        """Handle specialized nutrition queries"""
        return await self.nutrition_expert_agent.handle_message(input_lower, context)

    async def _handle_injury(self, input_lower: str, context: UserSessionContext) -> str:
        """Handle injury-related queries"""
        return await self.injury_support_agent.handle_message(input_lower, context)

    async def _route_command(self, input_lower: str, context: UserSessionContext) -> str:
        """Route command to appropriate handler"""
        for keywords, handler in self.command_handlers:
            if any(kw in input_lower for kw in keywords):
                return await handler(input_lower, context)
        return await analyze_goal(input_lower, context)

    async def _handle_schedule(self, input_lower: str, context: UserSessionContext) -> str:
        return await schedule_checkin(context)

    async def _handle_tracking(self, input_lower: str, context: UserSessionContext) -> str:
        return await log_activity(context) if input_lower.startswith("log ") else await track_progress(context)

    async def _handle_progress(self, input_lower: str, context: UserSessionContext) -> str:
        return await search_progress(context)

    async def _handle_workout(self, input_lower: str, context: UserSessionContext) -> str:
        return await recommend_workout(input_lower, context)

    async def _handle_nutrition(self, input_lower: str, context: UserSessionContext) -> str:
        return await generate_meal_plan(input_lower, context)

    def _format_error(self, error: Exception) -> str:
        """Format error message consistently"""
        error_type = type(error).__name__
        source_map = {
            "workout": "Workout Recommender",
            "meal": "Meal Planner",
            "track": "Progress Tracker",
            "schedule": "Scheduler"
        }
        error_source = next((v for k, v in source_map.items() if k in str(error).lower()), "Goal Analyzer")

        return (
            "⚠️ SYSTEM ERROR ⚠️\n\n"
            f"• <b>Source</b>: {error_source} module\n"
            f"• Error Type: {error_type}\n"
            f"• Details: {str(error)}\n\n"
            "🔧 Troubleshooting Checklist:\n"
            "1. Verify your input format\n"
            "2. Check required parameters\n"
            "3. Confirm service availability\n"
            "4. Try a simpler request\n\n"
            "🛠 Technical team has been notified"
        )