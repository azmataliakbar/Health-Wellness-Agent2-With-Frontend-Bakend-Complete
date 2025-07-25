# health_wellness_agent2/tools/workout_recommender.py
import asyncio
from context import UserSessionContext

async def recommend_workout(input: str, context) -> str:
    await asyncio.sleep(0)  # Makes it truly async

    workout_plans = {
        "beginner": [
            "🏋️ **Strength**: Bodyweight squats (3x10), Wall push-ups (3x8)",
            "🧘 **Flexibility**: Daily stretching (10 mins)",
            "🚶 **Cardio**: Brisk walking 20 mins (3x/week)"
        ],
        "intermediate": [
            "🏋️ **Strength**: Dumbbell rows (3x12), Lunges (3x10/side)",
            "🤸 **Mobility**: Dynamic stretches (15 mins)",
            "🏃 **Cardio**: Jogging 30 mins (3x/week)"
        ],
        "advanced": [
            "🏋️ **Strength**: Deadlifts (4x8), Pull-ups (3x max reps)",
            "🧗 **Plyometrics**: Box jumps (3x10), Burpees (3x15)",
            "⚡ **HIIT**: 30 sec sprint/90 sec walk (8 rounds)"
        ]
    }

    input_lower = input.lower()
    for level in workout_plans:
        if level in input_lower:
            workouts = "\n".join(workout_plans[level])
            return f"🏋️ **{level.capitalize()} Workout Plan**:\n\n{workouts}"

    # Fallback message
    return (
        "🔥 **General Fitness Guidance**:\n\n"
        "Experience Levels:\n"
        "• 🐣 Beginner (new to exercise)\n"
        "• 🌿 Intermediate (6+ months training)\n"
        "• 🦍 Advanced (2+ years consistent)\n\n"
        "💪 Try asking:\n"
        "- 'beginner workout plan'\n"
        "- 'intermediate training routine'\n"
        "- 'advanced exercise program'"
    )
