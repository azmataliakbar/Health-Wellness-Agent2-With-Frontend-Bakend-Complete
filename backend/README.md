
1-NextJs Frontend Chat Bot:

![Health Bot](/public/chat1.png)

2-API Backend Chat Web Page:

![API Screen](/public/chat2.png)


# 🧠 Health & Wellness Agent2 (Backend)

This is the backend for the **Health & Wellness Assistant**, built using **FastAPI** and enhanced with OpenAI for intelligent responses when local logic can't handle the query. It powers the frontend chat interface, delivering real-time fitness, nutrition, and wellness advice.

> 🌐 **Live API**:
> 🔗 [Backend URL](https://health-wellness-agent2-backend.onrender.com)
> 🔧 [Swagger Docs](https://health-wellness-agent2-backend.onrender.com/docs)

---

## ⚙️ Technologies Used

- 🐍 **Python 3.11+**
- ⚡ **FastAPI** – For async API endpoints
- 🔐 **OpenAI** – For AI-powered fallback answers
- 📦 **Pydantic** – Data validation
- 🧪 **Uvicorn** – ASGI web server
- 🌍 **CORS** enabled for full frontend-backend communication
- 🔐 **python-dotenv** – For secure API key management

---

## 📁 Project Structure
health_wellness_agent/
├── main.py # CLI chatbot interface with fallback logic
├── fast_api.py # FastAPI server exposing /query endpoint
├── agent.py # Core logic for health query handling
├── context.py # Session-based memory handling
├── guardrails.py # Input/output sanitization (optional)
├── requirements.txt # All dependencies
├── tools/ # Modular health tools (e.g. BMI, hydration)
└── agents/ # Specialized sub-agents

---

## 🔌 API Endpoints

### `GET /`
Returns service status and local documentation hint.

### `POST /query?user_input=...`
Handles a health query. First tries local logic. If not understood, falls back to OpenAI.

#### Example Response:
```json
{
  "response": "Drink at least 2-3 liters of water daily.",
  "source": "local",
  "tokens_used": null
}

```
#### If OpenAI is used:
```
{
  "response": "Include more fiber and vegetables in your diet.",
  "source": "openai",
  "tokens_used": 43
}

```
---

🧠 How It Works
Local Response First:
The HealthWellnessAgent checks if the query matches known health rules.

OpenAI Fallback:
If no local logic applies, it calls GPT-3.5-Turbo with strict formatting guidelines:

Short, clear facts

No medical diagnoses

Uses bullet points when instructional

Always recommends consulting a doctor for uncertain topics

Source Tagging:
Each response tells you if it came from "local" or "openai".

🖥️ Run Locally
1. Clone the Repo
git clone https://github.com/yourusername/health-wellness-backend.git
cd health-wellness-backend

2. Set Up Environment
Create a .env file:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


3. Install Dependencies
pip install -r requirements.txt

4. Run Server
uvicorn fast_api:app --reload

🔗 Visit http://127.0.0.1:8000/docs for Swagger UI
📡 CORS is enabled, so your frontend can connect seamlessly

🚀 Deployment (Render)
Push your code to GitHub.

Log into Render

Create a new Web Service:

Environment: Python 3

Start command: uvicorn fast_api:app --host 0.0.0.0 --port 10000

Add environment variable: OPENAI_API_KEY

Deploy and grab your public backend URL.

💡 Features
✅ Local + AI fallback logic
✅ OpenAI token tracking
✅ Bullet-format answers when instructional
✅ Works seamlessly with any frontend (React, Next.js, etc.)
✅ CLI chatbot for testing
✅ Error messages with full traceback for debugging

📦 requirements.txt
fastapi==0.100.1
uvicorn==0.23.2
openai==1.93.0
pydantic==2.11.5
python-dotenv==1.0.1


🤝 Connected Frontend
🔗 Frontend GitHub Repo
💬 Built with Next.js & TypeScript

🙏 Acknowledgements
Developed with ❤️ by Azmat Ali
Powered by FastAPI, OpenAI, and Render
Secure API communication via .env
Connected to a responsive chat frontend

🧪 Try the API
Example via curl:
curl -X POST "https://health-wellness-agent2-backend.onrender.com/query?user_input=how to lose weight"


📜 License
This project is for educational and informational use only. Always consult a professional for medical guidance.

🌍 Result:
Your backend (FastAPI) runs on Render ✅
Your frontend (Next.js) runs on Vercel ✅
User opens frontend → It talks to live backend → AI gives response ✅

🎯 Goal
Keep fast_api.py always online (as backend API)
Deploy Next.js frontend that communicates with the backend
Ensure both work even after system restart
# -------------------------------------------------------------
 Goal Setting Questions:
 "I want to lose 10 pounds in 2 months"
 "How can I build muscle effectively?"
 "My goal is to improve my endurance"
 Meal Plan Questions:
 "Can you suggest a vegetarian meal plan?"
 "I need gluten-free meal ideas"
 "What's a good vegan diet for weight loss?"
 Workout Questions:
 "Recommend a cardio workout routine"
 "Suggest strength training exercises"
 "What's a good HIIT workout?"
 Combination Questions:
 "I want to lose weight - suggest meals and workouts"
 "Help me build muscle with diet and exercise plans"
 General Health Questions:
 "What are some healthy breakfast options?"
 To Exit:
 Type "exit" or "quit" at any time
 The assistant will:
 Analyze your goals
 Provide personalized meal plans
 Recommend suitable workouts
 Maintain context during your conversation

# -------------------------------------------------------------

Prepared By : Azmat Ali Akbar

# -------------------------------------------------------------
Press Ctrl + Shift + P → type Python: Select Interpreter
https://health-wellness-agent2-backend.onrender.com/

https://health-wellness-agent2-backend.onrender.com/docs