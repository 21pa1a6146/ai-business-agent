from crewai.tools import BaseTool
from duckduckgo_search import DDGS

class DuckDuckGoTool(BaseTool):
    name: str = "Web Search"
    description: str = "Search the web for information about a company"

    def _run(self, query: str) -> str:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=5)
            output = ""
            for r in results:
                output += f"Title: {r['title']}\n"
                output += f"Summary: {r['body']}\n\n"
            return output

search_tool = DuckDuckGoTool()
