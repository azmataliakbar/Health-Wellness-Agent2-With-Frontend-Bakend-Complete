# health_wellness_agent2/tools/meal_planner.py
import asyncio
from context import UserSessionContext

async def generate_meal_plan(input: str, context) -> str:
    await asyncio.sleep(0)

    diet_plans = {
        "keto": [
            "🍳 **Breakfast**: Scrambled eggs with spinach and avocado",
            "🥗 **Lunch**: Grilled chicken salad with avocado and olive oil dressing",
            "🐟 **Dinner**: Grilled salmon with asparagus"
        ],
        "vegetarian": [
            "🥣 **Breakfast**: Oatmeal with almond milk and fresh berries",
            "🥗 **Lunch**: Chickpea salad with cucumbers and tomatoes",
            "🍛 **Dinner**: Lentil curry with brown rice"
        ],
        "vegan": [
            "🍳 **Breakfast**: Tofu scramble with bell peppers and spinach",
            "🥗 **Lunch**: Chickpea salad with lemon-tahini dressing",
            "🌶️ **Dinner**: Vegan chili with black beans and sweet potatoes"
        ],
        "gluten-free": [
            "🥣 **Breakfast**: Greek yogurt with honey and berries",
            "🥗 **Lunch**: Grilled chicken quinoa salad",
            "🐟 **Dinner**: Baked salmon with steamed broccoli"
        ]
    }

    input_lower = input.lower()
    for diet in diet_plans:
        if diet in input_lower:
            meals = "\n".join(diet_plans[diet])
            return f"🍽️ **{diet.capitalize()} Meal Plan**:\n\n{meals}"

    # Fallback message
    return (
        "🍏 **General Nutrition Guidance**:\n\n"
        "Popular Diets:\n"
        "• 🥦 Vegetarian (plant-based + dairy/eggs)\n"
        "• 🌱 Vegan (100% plant-based)\n"
        "• 🚫 Gluten-Free (no wheat/barley/rye)\n"
        "• 🥩 Keto (low-carb, high-fat)\n\n"
        "💡 Try asking:\n"
        "- 'keto or vegan or vegetarian or gluten-Free food / diet / meal'\n"
        "- 'common or general food / diet / meal'"
    )