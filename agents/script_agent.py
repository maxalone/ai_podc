import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class ScriptAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_script(self, topic: str) -> str:
        """Genera il copione del podcast su un tema specifico."""
        prompt = f"""
        Crea un copione per un episodio di podcast sul tema "{topic}".
        Deve avere: introduzione, corpo, conclusione e durata stimata di 5 minuti.
        Linguaggio naturale, ritmo fluido, tono narrativo e divulgativo.
        """
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()
