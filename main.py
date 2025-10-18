from agents.orchestrator import Orchestrator

if __name__ == "__main__":
    topic = input("Inserisci il tema del podcast: ")
    orchestrator = Orchestrator()
    result = orchestrator.run(topic)

    print("\n=== RISULTATI ===")
    print(result["script"][:500], "...\n")
    print(result["posts"])
    print(f"\nAudio salvato in: {result['audio_path']}")
