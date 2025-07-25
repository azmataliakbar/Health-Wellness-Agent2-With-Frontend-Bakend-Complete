# health_wellness_agent2/tools/goal_analyzer.py
import asyncio
from context import UserSessionContext

async def analyze_goal(input: str, context) -> str:
    await asyncio.sleep(0)
    input_lower = input.lower()
    
    # Weight Loss/Fat Reduction
    if any(word in input_lower for word in [
        "lose", "weight loss", "fat", "slim", "lean",
        "burn fat", "reduce weight", "cutting"
    ]):
        return (
            "⚖️ **Weight Loss Plan**\n\n"
            "1. 🏃 Cardio 3-5x weekly (walking/running)\n"
            "2. 🍽 Moderate calorie deficit (300-500cal)\n"
            "3. 🥩 High-protein meals (1.6-2.2g/kg)\n"
            "4. 🏋️ Strength training to maintain muscle\n\n"
            "💡 Pro Tip: Track measurements weekly, not just weight!"
        )
    
    # Weight Gain
    elif any(word in input_lower for word in [
        "gain weight", "increase weight", "put on weight", 
        "weight gain", "bulk up", "add pounds"
    ]):
        return (
            "📈 **Healthy Weight Gain**\n\n"
            "1. 🍌 Calorie surplus (300-500cal above maintenance)\n"
            "2. 🏋️ Strength training 3-4x weekly\n"
            "3. 🍗 Protein-rich meals (1.6-2.2g/kg)\n"
            "4. 🍠 Healthy carbs (rice, oats, potatoes)\n"
            "5. 📊 Track progress weekly\n\n"
            "💡 Pro Tip: Aim for 0.5-1lb gain per week"
        )
    
    # Muscle Building
    elif any(word in input_lower for word in [
        "build", "muscle", "gain mass", "bulk",
        "get bigger", "hypertrophy"
    ]):
        return (
            "💪 **Muscle Building**\n\n"
            "1. 🔝 Progressive overload training\n"
            "2. 🏋️ Compound lifts (squats, deadlifts)\n"
            "3. 🥩 High-protein diet (1.6-2.2g/kg)\n"
            "4. 🍚 Calorie surplus (200-500cal)\n"
            "5. 😴 7-9 hours sleep nightly\n\n"
            "💡 Pro Tip: Focus on 8-12 rep range for hypertrophy"
        )
    
    # General Fitness
    elif any(word in input_lower for word in [
        "fitness", "tone", "endurance", "get fit",
        "in shape", "toned"
    ]):
        return (
            "🌟 **General Fitness**\n\n"
            "1. 🔀 Mix strength & cardio\n"
            "2. 🏋️ Full-body workouts 3x weekly\n"
            "3. 🥗 Balanced nutrition\n"
            "4. 🧘 Include flexibility work\n\n"
            "💡 Pro Tip: Try circuit training for efficiency"
        )
    
    # Strength Training
    elif any(word in input_lower for word in [
        "strength", "power", "get stronger",
        "lift more", "powerlifting"
    ]):
        return (
            "🏆 **Strength Training**\n\n"
            "1. 🏋️ Heavy compound lifts\n"
            "2. 🔢 Low reps (3-6) with max weight\n"
            "3. ⏳ Longer rest between sets (2-5min)\n"
            "4. 👀 Focus on form first\n\n"
            "💡 Pro Tip: Deload every 4-6 weeks"
        )
    
    # Health/Wellness
    elif any(word in input_lower for word in [
        "health", "wellness", "healthy lifestyle",
        "wellbeing", "overall health"
    ]):
        return (
            "🌿 **Holistic Health**\n\n"
            "1. 🥗 Balanced whole-food diet\n"
            "2. 🏃 150min exercise weekly\n"
            "3. 😴 7-9 hours quality sleep\n"
            "4. 🧘 Stress management\n\n"
            "💡 Pro Tip: Morning sunlight boosts circadian rhythm"
        )
    
    else:
        return (
            "❓ **Goal Analysis**\n\n"
            "Common Goal Types:\n"
            "• ⚖️ Weight Loss\n"
            "• 📈 Weight Gain\n"
            "• 💪 Muscle Building\n"
            "• 🏆 Strength Training\n"
            "• 🌿 General Health\n\n"
            "💡 Try: 'How to lose weight?' or 'Best muscle building plan?'"
        )