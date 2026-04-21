from crewai import Task
from agents import researcher, analyst, writer

def create_tasks(company_name: str):
    research_task = Task(
        description=f"""
        Research the company: {company_name}
        Find the following:
        1. What the company does
        2. Recent news (last 6 months)
        3. Key competitors
        4. Revenue or market position
        5. Any major challenges
        """,
        expected_output="A detailed research summary with 5 sections",
        agent=researcher
    )

    analysis_task = Task(
        description=f"""
        Analyze the research about {company_name}:
        1. SWOT analysis
        2. Market position score (1-10)
        3. Top 3 risks
        4. Top 3 opportunities
        5. Rating: Buy / Hold / Avoid
        """,
        expected_output="Structured analysis with SWOT and ratings",
        agent=analyst,
        context=[research_task]
    )

    report_task = Task(
        description=f"""
        Write a professional report about {company_name}.
        Format it like this:
        # Business Report: {company_name}
        ## Executive Summary
        ## Company Overview
        ## Market Position
        ## SWOT Analysis
        ## Key Risks
        ## Opportunities
        ## Recommendation

        Return the complete report as plain text only.
        Do NOT use any file writing tools.
        """,
        expected_output="Complete formatted business report as text",
        agent=writer,
        context=[research_task, analysis_task]
    )

    return [research_task, analysis_task, report_task]