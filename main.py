from crewai import Crew, Process
from agents import researcher, analyst, writer
from tasks import create_tasks
import time

def run_business_research(company_name: str):

    print(f"\n{'='*50}")
    print(f"  Starting Research for: {company_name}")
    print(f"{'='*50}\n")

    tasks = create_tasks(company_name)

    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    # Save report manually to file
    filename = f"{company_name.lower().replace(' ', '_')}_report.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(result))

    print(f"\n{'='*50}")
    print(f"  Research Complete!")
    print(f"  Report saved as: {filename}")
    print(f"{'='*50}\n")

    return result

if __name__ == "__main__":
    company = input("Enter a company name to research: ")
    print("Starting research...")
    time.sleep(3)
    run_business_research(company)