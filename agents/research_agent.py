import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv('.env.local')

class ResearchAgent:
    def __init__(self):
        self.client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    def search_topic(self, topic: str) -> str:
        """Recupera informazioni aggiornate sul tema scelto."""
        try:
            results = self.client.search(topic)
            summary = "\n".join([r["content"] for r in results["results"][:3]])
            return summary
        except Exception as e:
            return f"Errore nella ricerca: {e}"
