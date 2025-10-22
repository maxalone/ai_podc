import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv('.env.local')

class SocialAgent:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY non trovata in .env.local")
        
        self.client = Groq(api_key=self.api_key)

    def create_social_posts(self, topic: str, script: str) -> dict:
        """Genera post per social media basati sul copione del podcast."""
        
        prompt = f"""Basandoti su questo copione di podcast sul tema "{topic}":

{script[:1000]}...

Crea 3 post per social media:

1. **LinkedIn** (professionale, 200-300 caratteri)
2. **Twitter/X** (conciso, max 280 caratteri, con 2-3 hashtag)
3. **Instagram** (coinvolgente, 150-200 caratteri, con emoji e 3-5 hashtag)

Ogni post deve:
- Catturare l'attenzione
- Includere un takeaway chiave
- Invitare all'ascolto del podcast

Formato risposta:
[LINKEDIN]
testo del post

[TWITTER]
testo del post

[INSTAGRAM]
testo del post"""

        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "Sei un esperto di social media marketing. Crei post coinvolgenti e ottimizzati per ogni piattaforma."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.8,
                max_tokens=1000,
                top_p=0.9
            )
            
            content = response.choices[0].message.content
            
            # Parse i post dai tag
            posts = {
                "linkedin": self._extract_section(content, "LINKEDIN"),
                "twitter": self._extract_section(content, "TWITTER"),
                "instagram": self._extract_section(content, "INSTAGRAM")
            }
            
            return posts
                
        except Exception as e:
            raise Exception(f"Errore generazione post social con Groq: {e}")
    
    def _extract_section(self, text: str, section_name: str) -> str:
        """Estrae una sezione specifica dal testo."""
        try:
            start = text.find(f"[{section_name}]")
            if start == -1:
                return f"Post per {section_name} non generato"
            
            start += len(f"[{section_name}]")
            
            # Trova la prossima sezione o la fine del testo
            next_section = len(text)
            for tag in ["[LINKEDIN]", "[TWITTER]", "[INSTAGRAM]"]:
                pos = text.find(tag, start)
                if pos != -1 and pos < next_section:
                    next_section = pos
            
            content = text[start:next_section].strip()
            return content if content else f"Post per {section_name} non generato"
            
        except Exception:
            return f"Errore nell'estrazione del post {section_name}"