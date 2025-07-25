# health_wellness_agent2/agents/nutrition_expert_agent.py

from typing import Any, Dict
from context import UserSessionContext
import asyncio

class NutritionExpertAgent:
    """Specialized agent for nutrition and dietary concerns with colorful formatting"""
    
    # Define constants for dietary conditions
    DIABETES = "diabetes"
    HYPERTENSION = "hypertension"
    ALLERGIES = "allergies"
    WEIGHT_LOSS = "weight loss"
    ENERGY_BOOST = "energy boost"

    def __init__(self):
        self.dietary_conditions = {
            self.DIABETES: {
                "avoid": ["🍬 High sugar foods", "🍞 Refined carbs", "🥤 Sugary drinks", "🍞 White bread"],
                "recommend": ["🌾 Whole grains", "🍗 Lean proteins", "🥦 Non-starchy vegetables", "🥑 Healthy fats"],
                "tips": ["📊 Monitor blood sugar regularly", "⏰ Eat at consistent times", "🍽️ Control portion sizes"]
            },
            self.HYPERTENSION: {
                "avoid": ["🧂 High sodium foods", "🥓 Processed meats", "🥫 Canned soups", "🍔 Fast food"],
                "recommend": ["🍎 Fresh fruits", "🥕 Vegetables", "🌾 Whole grains", "🥛 Low-fat dairy"],
                "tips": ["🧂 Limit sodium to 2300mg/day", "🌿 Use herbs and spices", "🏷️ Read nutrition labels"]
            },
            self.ALLERGIES: {
                "avoid": ["⚠️ Known allergens", "🔄 Cross-contaminated foods", "🏷️ Unclear ingredient foods"],
                "recommend": ["🍎 Fresh whole foods", "🏷️ Clearly labeled products", "🏠 Home-cooked meals"],
                "tips": ["👀 Always read labels", "💊 Carry emergency meds", "🍽️ Inform restaurants"]
            },
            self.WEIGHT_LOSS: {
                "avoid": ["🍟 Fried foods", "🍰 Sugary desserts", "🥤 Sweetened beverages", "🍕 Fast food"],
                "recommend": ["🥗 High-volume veggies", "🍗 Lean proteins", "🌰 Healthy fats", "💧 Water"],
                "tips": ["⚖️ Track portions", "⏲️ Eat mindfully", "🏃 Combine with exercise"]
            },
            self.ENERGY_BOOST: {
                "avoid": ["☕ Excess caffeine", "🍬 Sugar crashes", "🍞 Refined carbs", "🍔 Heavy meals"],
                "recommend": ["🍌 Potassium-rich foods", "🥜 Healthy fats", "💧 Hydration", "🌿 Iron-rich foods"],
                "tips": ["⏰ Eat small frequent meals", "💤 Prioritize sleep", "🧘 Manage stress"]
            }
        }

    async def handle_message(self, message: str, context: UserSessionContext) -> str:
        """Process nutrition-related concerns with async support"""
        await asyncio.sleep(0.1)  # Simulate async processing
        
        print(f"\n🥗 Nutrition query: {message[:50]}...")
        
        try:
            if hasattr(context, 'add_handoff_log'):
                context.add_handoff_log("main", "nutrition_expert", f"Nutrition: {message[:50]}...")
        except Exception :
            pass  # Silently ignore if logging fails
        
        condition = self._identify_dietary_condition(message)
        
        if condition in self.dietary_conditions:
            return self._generate_condition_specific_advice(condition)
        
        return self._generate_general_nutrition_advice()

    def _identify_dietary_condition(self, message: str) -> str:
        """Identify dietary condition from message"""
        message_lower = message.lower()
        
        condition_keywords = {
            self.DIABETES: ["diabetes", "diabetic", "blood sugar", "glucose"],
            self.HYPERTENSION: ["blood pressure", "hypertension", "high bp"],
            self.ALLERGIES: ["allergy", "allergic", "intolerance"],
            self.WEIGHT_LOSS: ["lose weight", "weight loss", "slimming", "dieting"],
            self.ENERGY_BOOST: ["energy", "fatigue", "tired", "low energy"]
        }
        
        for condition, keywords in condition_keywords.items():
            if any(kw in message_lower for kw in keywords):
                return condition
        
        return "unknown"

    def _generate_condition_specific_advice(self, condition: str) -> str:
        """Generate colorful advice for specific conditions"""
        info = self.dietary_conditions[condition]
        
        return (
            f"🍏 **{condition.upper()} NUTRITION GUIDE** 🍎\n\n"
            f"🚫 **AVOID These:**\n"
            f"{chr(10).join(info['avoid'])}\n\n"
            f"✅ **ENJOY These Instead:**\n"
            f"{chr(10).join(info['recommend'])}\n\n"
            f"💡 **Smart Tips:**\n"
            f"{chr(10).join(info['tips'])}\n\n"
            f"⏳ **Daily Habits:**\n"
            "• Eat regular meals at consistent times\n"
            "• Stay hydrated with water\n"
            "• Get enough sleep for metabolic health\n"
            "• Manage stress through mindful eating\n\n"
            f"📅 **{condition.title()} Meal Plan Example:**\n"
            "🍳 Breakfast: Protein + fiber combo\n"
            "🥗 Lunch: Balanced plate with veggies\n"
            "🍽️ Dinner: Light and nutrient-dense\n"
            "🍎 Snacks: Healthy options between meals"
        )

    def _generate_general_nutrition_advice(self) -> str:
        """Generate comprehensive general nutrition advice"""
        return (
            "🌟 **ESSENTIAL NUTRITION PRINCIPLES** 🌟\n\n"
            "🍎 **Daily Food Goals:**\n"
            "• 5-9 servings fruits/veggies\n"
            "• 6-8 servings whole grains\n"
            "• 2-3 servings lean protein\n"
            "• Healthy fats in moderation\n\n"
            "💧 **Hydration Targets:**\n"
            "• 8+ glasses water daily\n"
            "• More if active/sweating\n"
            "• Limit sugary drinks\n\n"
            "⏰ **Healthy Eating Patterns:**\n"
            "• Consistent meal times\n"
            "• Balanced macronutrients\n"
            "• Mindful eating practices\n"
            "• Proper portion sizes\n\n"
            "📊 **Nutrition Tracking:**\n"
            "• Food journal for awareness\n"
            "• Note energy/mood with foods\n"
            "• Adjust based on results\n\n"
            "🏆 **Specialized Guidance Available For:**\n"
            f"• {self.DIABETES.capitalize()} management 🩸\n"
            f"• {self.HYPERTENSION.capitalize()} ❤️\n"
            f"• {self.ALLERGIES.capitalize()} 🚫\n"
            f"• {self.WEIGHT_LOSS.capitalize()} goals ⚖️\n"
            f"• {self.ENERGY_BOOST.capitalize()} optimization ⚡\n\n"
            "💬 Ask me about any specific nutrition needs!"
        )
    