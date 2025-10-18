import os
from elevenlabs import ElevenLabs
from dotenv import load_dotenv

load_dotenv()

class TTSAgent:
    def __init__(self):
        self.client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

    def text_to_speech(self, text: str, output_path="output.mp3"):
        """Converte un testo in voce e salva l'audio."""
        audio = self.client.text_to_speech.convert(
            voice="Rachel",  # voce predefinita (puoi cambiarla)
            text=text,
            model="eleven_multilingual_v2"
        )
        with open(output_path, "wb") as f:
            f.write(audio)
        return output_path
