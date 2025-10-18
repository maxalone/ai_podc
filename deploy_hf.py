import os
import sys
from dotenv import load_dotenv
from huggingface_hub import HfApi, Repository

# Carica le variabili d'ambiente
load_dotenv()

def get_token():
    """Cerca il token in questo ordine:
    1. Variabili d'ambiente del sistema
    2. File .env
    3. GitHub Secrets (già passate come env vars)
    """
    # Prova diversi nomi per il token
    token = (
        os.getenv('HF_TOKEN') or
        os.getenv('HUGGINGFACE_TOKEN') or
        os.getenv('HUGGING_FACE_HUB_TOKEN') or
        os.getenv('HF_API_TOKEN')
    )
    
    if not token:
        print("ERRORE: Nessun token di Hugging Face trovato!")
        print("Assicurati di aver impostato una di queste variabili:")
        print("HF_TOKEN, HUGGINGFACE_TOKEN, HUGGING_FACE_HUB_TOKEN, HF_API_TOKEN")
        sys.exit(1)
    
    return token

def deploy_to_huggingface():
    try:
        # Ottieni il token
        token = get_token()
        
        # Configura l'API
        api = HfApi(token=token)
        
        # Crea o aggiorna il repository
        repo_name = os.getenv('REPO_NAME', 'my-model')
        repo_url = api.create_repo(
            repo_id=repo_name,
            exist_ok=True,
            private=False  # Cambia a True se vuoi privato
        )
        
        print(f"Repository Hugging Face: {repo_url}")
        
        # Qui aggiungi la logica specifica per il tuo deploy
        # Esempio: caricare modelli, dataset, ecc.
        
        print("Deploy su Hugging Face completato con successo!")
        
    except Exception as e:
        print(f"Errore durante il deploy su Hugging Face: {e}")
        sys.exit(1)

if __name__ == "__main__":
    deploy_to_huggingface()