from agents.script_agent import ScriptAgent
from agents.research_agent import ResearchAgent
from agents.social_agent import SocialAgent
from agents.tts_agent import TTSAgent

class Orchestrator:
    def __init__(self):
        self.script_agent = ScriptAgent()
        self.research_agent = ResearchAgent()
        self.social_agent = SocialAgent()
        self.tts_agent = TTSAgent()

    def run(self, topic: str):
        print(f"🎙️ Generazione podcast sul tema: {topic}\n")

        # 1. Ricerca
        research = self.research_agent.search_topic(topic)
        print("🔍 Ricerca completata.")

        # 2. Copione
        script = self.script_agent.generate_script(topic + "\n\n" + research)
        print("🧠 Script generato.")

        # 3. Post social
        posts = self.social_agent.create_social_posts(topic, script)
        print("📱 Contenuti social creati.")

        # 4. TTS
        audio_path = self.tts_agent.text_to_speech(script)
        print(f"🎧 Audio generato in: {audio_path}")

        return {
            "topic": topic,
            "script": script,
            "posts": posts,
            "audio_path": audio_path
        }
