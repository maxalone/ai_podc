from agents.orchestrator import Orchestrator

def main():
    print("Hello from podcast-agents!")


if __name__ == "__main__":
    orchestrator = Orchestrator()
    orchestrator.run(topic="AI nella musica contemporanea")