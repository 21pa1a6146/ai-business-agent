from crewai import Agent, LLM
from tools import search_tool, file_writer
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

researcher = Agent(
    role="Senior Business Researcher",
    goal="Find accurate up-to-date information about a company",
    backstory="""You are an expert business analyst at a top
    consulting firm. You are thorough and precise.""",
    tools=[search_tool],
    llm=llm,
    verbose=True,
    max_iter=10
)

analyst = Agent(
    role="Business Strategy Analyst",
    goal="Analyze research data and extract key business insights",
    backstory="""You are a strategic analyst who transforms raw
    data into clear business narratives.""",
    tools=[],
    llm=llm,
    verbose=True
)

writer = Agent(
    role="Executive Report Writer",
    goal="Write professional business reports",
    backstory="""You write crisp structured reports used by
    C-suite executives.""",
    tools=[file_writer],
    llm=llm,
    verbose=True
)