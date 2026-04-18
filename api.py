from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from crewai import Crew, Process
from agents import researcher, analyst, writer
from tasks import create_tasks
from tracker import track_research
import time
import traceback

app = FastAPI(title="AI Business Research API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")

class ResearchRequest(BaseModel):
    company: str

@app.get("/")
def home():
    return FileResponse("frontend/index.html")

@app.post("/research")
def research_company(request: ResearchRequest):
    company = request.company
    print(f"🔍 Researching: {company}")
    start_time = time.time()

    try:
        tasks = create_tasks(company)
        crew = Crew(
            agents=[researcher, analyst, writer],
            tasks=tasks,
            process=Process.sequential,
            verbose=False
        )
        result = crew.kickoff()
        duration = time.time() - start_time

        try:
            track_research(company, str(result), duration)
        except Exception as mlflow_err:
            print(f"⚠️ MLflow tracking failed: {mlflow_err}")

        filename = f"{company.lower().replace(' ', '_')}_report.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(result))

        return {
            "company": company,
            "report": str(result),
            "duration": round(duration, 2),
            "status": "success"
        }

    except Exception as e:
        traceback.print_exc()
        print(f"❌ Error during research: {e}")
        return {
            "company": company,
            "report": "",
            "duration": 0,
            "status": "error",
            "message": str(e)
        }