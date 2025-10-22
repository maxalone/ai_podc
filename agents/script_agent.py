import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv('.env.local')

class ScriptAgent:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY non trovata in .env.local")
        
        # Inizializza il client Groq
        self.client = Groq(api_key=self.api_key)

    def generate_script(self, topic: str) -> str:
        """Genera il copione del podcast su un tema specifico usando Groq."""
        
        prompt = f"""Crea un copione per un episodio di podcast in italiano sul tema "{topic}".
Il copione deve avere:
- Introduzione coinvolgente
- Corpo principale con 3 punti chiave
- Conclusione con takeaway
- Durata stimata: 5 minuti
- Linguaggio naturale e divulgativo
- Tono narrativo e fluido

Struttura:
[INTRO]
[CONTENUTO PRINCIPALE] 
[CONCLUSIONE]"""
        
        try:
            # Chiamata API Groq
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",  # Modello migliore gratuito
                messages=[
                    {
                        "role": "system",
                        "content": "Sei un esperto scrittore di podcast educativi in italiano. Crei copioni coinvolgenti e ben strutturati."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=2000,
                top_p=0.9
            )
            
            # Estrai il testo generato
            generated_text = response.choices[0].message.content
            return generated_text.strip()
                
        except Exception as e:
            raise Exception(f"Errore generazione script con Groq: {e}")