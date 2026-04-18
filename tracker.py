import mlflow
import time

def track_research(company_name: str, result: str, duration: float):
    mlflow.set_experiment("AI Business Research")
    
    with mlflow.start_run():
        # Log what company was researched
        mlflow.log_param("company", company_name)
        
        # Log how long it took
        mlflow.log_metric("duration_seconds", duration)
        
        # Log the report as a file
        with open("report.txt", "w") as f:
            f.write(result)
        mlflow.log_artifact("report.txt")
        
    print(f"✅ Run tracked in MLflow for: {company_name}")