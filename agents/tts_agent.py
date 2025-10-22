import os
from elevenlabs.client import ElevenLabs
from elevenlabs import save
from dotenv import load_dotenv

load_dotenv('.env.local')

class TTSAgent:
    def __init__(self):
        api_key = os.getenv("ELEVENLABS_API_KEY")
        if not api_key:
            raise ValueError("ELEVENLABS_API_KEY non trovata in .env.local")
        
        self.client = ElevenLabs(api_key=api_key)

    def text_to_speech(self, text: str, output_path="output.mp3"):
        """Converte un testo in voce e salva l'audio."""
        try:
            # Metodo corretto per l'API ElevenLabs più recente
            audio = self.client.text_to_speech.convert(
                voice_id="EXAVITQu4vr4xnSDxMaL",  # Rachel (voce predefinita)
                text=text,
                model_id="eleven_multilingual_v2"
            )
            
            # Salva l'audio usando la funzione save di elevenlabs
            save(audio, output_path)
            
            print(f"🔊 Audio generato: {output_path}")
            return output_path
            
        except Exception as e:
            raise Exception(f"Errore generazione audio con ElevenLabs: {e}")