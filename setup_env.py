import os
from dotenv import load_dotenv

def setup_environment():
    """Setup dell'ambiente per sviluppo locale"""
    load_dotenv()
    
    # Verifica che tutte le variabili necessarie esistano
    required_vars = {
        'RAILWAY_TOKEN': 'Railway',
        'HF_TOKEN': 'Hugging Face',
    }
    
    missing_vars = []
    for var, service in required_vars.items():
        if not os.getenv(var):
            missing_vars.append(f"{var} ({service})")
    
    if missing_vars:
        print("ATTENZIONE: Variabili mancanti nel file .env:")
        for var in missing_vars:
            print(f"  - {var}")
        print("\nAssicurati di aver creato il file .env dal template .env.example")
        return False
    
    print("Tutte le variabili d'ambiente sono configurate correttamente!")
    return True

if __name__ == "__main__":
    setup_environment()