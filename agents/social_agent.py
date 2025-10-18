import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class SocialAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def create_social_posts(self, topic: str, summary: str) -> dict:
        """Crea post brevi per X, Instagram e LinkedIn."""
        prompt = f"""
        Crea tre brevi post per promuovere un podcast sul tema "{topic}".
        Usa il seguente riassunto per ispirarti:
        {summary}
        
        Formato:
        - X: (massimo 280 caratteri)
        - Instagram: (tono più evocativo)
        - LinkedIn: (tono professionale e riflessivo)
        """
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        content = response.choices[0].message.content.strip()
        return {"posts": content}
