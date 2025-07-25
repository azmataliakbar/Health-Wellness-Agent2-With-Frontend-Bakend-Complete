from pydantic import BaseModel, validator
from typing import Optional, Dict, List
import re

class GoalInput(BaseModel):
    """
    Input guardrail for validating user goal format.
    Example valid input: "lose 5kg in 2 months"
    """
    description: str
    
    @validator('description')
    def validate_goal_format(cls, v):
        pattern = r"(lose|gain|build|improve)\s+\d+\s*(kg|lbs|%|pounds)?\s*(in|within|for)\s+\d+\s*(weeks|months|days|years)"
        if not re.search(pattern, v, re.IGNORECASE):
            raise ValueError("Goal must be in format: [action] [amount] [unit] in [timeframe]. Example: 'lose 5kg in 2 months'")
        return v

class DietaryInput(BaseModel):
    """
    Input guardrail for dietary preferences
    """
    preference: str
    
    @validator('preference')
    def validate_dietary(cls, v):
        valid_options = ["vegetarian", "vegan", "gluten-free", "dairy-free", 
                        "keto", "paleo", "mediterranean", "none"]
        if v.lower() not in valid_options:
            raise ValueError(f"Dietary preference must be one of: {', '.join(valid_options)}")
        return v.lower()

class WorkoutOutput(BaseModel):
    """
    Output guardrail for workout recommendations
    """
    plan_name: str
    days: Dict[str, List[str]]
    equipment_needed: List[str]
    duration_weeks: int
    difficulty: str