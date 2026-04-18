# 🤖 AI Business Research Agent
An intelligent multi-agent system that generates comprehensive business research reports using AI. Just enter a company name and 3 AI agents collaborate to deliver instant business intelligence.

## ✨ Features
- 🔍 **Researcher Agent** — Gathers real-time company data from the web
- 📊 **Analyst Agent** — Performs SWOT analysis and financial overview
- ✍️ **Writer Agent** — Compiles everything into a structured professional report
- 🎨 **Beautiful UI** — Animated AI agent background with colorful orbs
- 📥 **Download Reports** — Save any report as a text file

## 📋 Report Sections Generated
1. Executive Summary
2. Company Overview
3. Products & Services
4. Financial Performance
5. SWOT Analysis
6. Competitive Landscape
7. Recent News & Developments
8. Future Outlook

## 🛠️ Tech Stack
- **Backend** — Python, FastAPI
- **AI Agents** — CrewAI
- **LLM** — Groq (llama-3.3-70b)
- **Frontend** — HTML, CSS, JavaScript
- **Deployment** — Render

## 🚀 Run Locally
git clone https://github.com/21pa1a6146/ai-business-agent.git
cd ai-business-agent
pip install -r requirements.txt
uvicorn api:app --reload

## ⚠️ Rate Limits (Groq Free Tier)
- ~50-80 reports per day
- If limit hit, wait 20 seconds and try again

## 👤 Author
Built with ❤️ using CrewAI and FastAPI
