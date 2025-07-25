
1-NextJs Frontend Chat Bot:

![Health Bot](/public/chat1.png)

2-API Backend Chat Web Page:

![API Screen](/public/chat2.png)


# 🌿 Health & Wellness Assistant (Frontend)

This is the frontend for the **Health & Wellness Assistant** project, built using **Next.js** and deployed on **Netlify**. It connects to a Python-based **FastAPI backend** hosted on **Render** to provide intelligent responses about fitness, diet, and wellness.

---

## 📁 Project Structure
📦 health-wellness-frontend
├── pages/
│ ├── api/
│ │ └── chat.ts # API route to communicate with FastAPI backend
│ └── page.tsx # Main chat interface page
├── public/
│ └── h2.png # Health bot image
├── styles/
│ └── HealthChat.module.css # CSS styles for the chat interface
├── types/
│ └── index.ts # TypeScript interfaces
├── .env.local # Environment variable to store backend URL
├── README.md # Project documentation
└── globals.css # Global CSS styles


---

## 🚀 Deployment Links

- 🔗 **Frontend (Next.js on Netlify)**: [🌐 Visit Site](https://your-netlify-app-url.netlify.app)
- 🔗 **Backend (FastAPI on Render)**: [🌐 API Endpoint](https://health-wellness-agent2-backend.onrender.com)

---

## ⚙️ Technologies Used

- **Next.js 13+ (App Router)**
- **TypeScript**
- **CSS Modules**
- **FastAPI (Python backend)**
- **Render (Backend Deployment)**
- **Netlify (Frontend Deployment)**

---

## 📡 How It Works

1. The user types a health-related question into the chat interface.
2. The frontend sends a `POST` request to the internal API route `/api/chat`.
3. This route fetches the response from the FastAPI backend via:

NEXT_PUBLIC_BACKEND_URL/query?user_input=...

4. The backend processes the request using local or OpenAI-based logic and returns a structured response.
5. The frontend displays the bot's reply in a styled chat interface, along with:
- 🔹 Source: "Local Knowledge" or "AI Generated"
- 🔸 Token count (if AI was used)

---

## 💡 Features

✅ Real-time health assistant
✅ Attractive and friendly UI
✅ Fully responsive for all screen sizes: **mobile, tablet, and desktop**
✅ Source tagging (local/AI)
✅ Error handling and typing indicators
✅ FastAPI backend integration via environment variable

---

## 🌐 Mobile & Responsive UI

📱 This frontend was designed with mobile-first principles and tested on:
- Android and iOS phones
- Tablets
- Laptops and desktops

💡 The layout adapts gracefully with clean fonts, spacing, and responsive chat elements.

---

## 📦 Environment Variable

To communicate with the backend, create a `.env.local` file with this content:

```env
NEXT_PUBLIC_BACKEND_URL=https://health-wellness-agent2-backend.onrender.com

✅ This ensures backend URL can be accessed securely in the frontend.
```
## To run the app locally:

## 1. Clone the repo
git clone https://github.com/yourusername/health-wellness-frontend.git
cd health-wellness-frontend

## 2. Install dependencies
npm install

## 3. Set up environment
touch .env.local
# Add the backend URL in .env.local

## 4. Run the app
npm run dev
# ---------------------------------------------

## 🌍 Deployment Process
✅ Netlify Steps:
Push your frontend code to GitHub.

Log in to Netlify.
Select "New site from Git" and connect your GitHub repository.
Set build command: npm run build
Set publish directory: out or .next
Add environment variable: NEXT_PUBLIC_BACKEND_URL
Click Deploy Site

✅ Site will be auto-redeployed on every Git push.


## ✨ Special Note
This frontend integrates seamlessly with our intelligent FastAPI backend to provide:

## 📋 Health tips
## 🏃‍♂️ Exercise advice
## 🥗 Nutrition plans
## 🤖 AI-based responses (when needed)

Designed to give users a smooth and helpful experience across all platforms.

## 🙏 Acknowledgement
Developed with ❤️ by Azmat Ali
Connected to Python backend via API
Deployed using Render & Netlify

## Check Backend url

https://health-wellness-agent2-backend.onrender.com/
https://health-wellness-agent2-backend.onrender.com/docs
