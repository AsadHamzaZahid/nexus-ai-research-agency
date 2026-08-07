from langchain.agents import create_agent
from dotenv import load_dotenv
import os
from tavily import TavilyClient
from langchain_community.tools import tool
from rich import print
import requests
from bs4 import BeautifulSoup
from langchain_core.tools import tool


load_dotenv()


Tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def web_search(query: str) -> str:
    "search thr web and return title ,url and snippet"
    results = Tavily.search(query=query, max_results=5)

    out = []

    for r in results['results']:
        out.append(f"title:{r["title"]} \n url: {r['url']} \n snippet: {r['content'][:300]} \n "

                   )

        return "\n--------\n".join(out)


@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""

    try:
        resp = requests.get(
            url,
            timeout=8,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        soup = BeautifulSoup(resp.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        return soup.get_text(separator=" ", strip=True)[:3000]

    except Exception as e:
        return f"Could not scrape URL: {str(e)}"


# print(web_search.invoke("what are top 5 artists of this century?"))

print(scrape_url.invoke(
    'https://www.billboard.com/lists/taylor-swift-top-artists-21st-century-chart/bruno-mars-10/'))
