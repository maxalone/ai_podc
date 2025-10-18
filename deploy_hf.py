import os
import sys
from dotenv import load_dotenv
from huggingface_hub import HfApi

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
        print("❌ ERRORE: Nessun token di Hugging Face trovato!")
        print("Assicurati di aver impostato una di queste variabili:")
        print("HF_TOKEN, HUGGINGFACE_TOKEN, HUGGING_FACE_HUB_TOKEN, HF_API_TOKEN")
        print("Se stai usando GitHub Actions, aggiungile nei Secrets del repository")
        return None  # Cambiato da sys.exit(1) a return None
    
    return token

def deploy_to_huggingface():
    try:
        # Ottieni il token
        token = get_token()
        
        if not token:
            # Nel workflow, non far fallire tutto il deploy se manca HF
            print("⚠️  Saltando deploy su Hugging Face - token non disponibile")
            return
        
        # Configura l'API
        api = HfApi(token=token)
        
        # Crea o aggiorna il repository
        repo_name = os.getenv('REPO_NAME', 'my-model')
        
        # ⚠️ IMPORTANTE: Aggiungi il tuo username!
        # Altrimenti proverà creare un repo sotto l'organization invece che sotto il tuo account
        your_username = "MaxAlone"  # SOSTITUISCI con il tuo username HF!
        repo_id = f"{your_username}/{repo_name}"
        
        repo_url = api.create_repo(
            repo_id=repo_id,  # Cambiato da repo_name a repo_id
            exist_ok=True,
            private=False  # Cambia a True se vuoi privato
        )
        
        print(f"✅ Repository Hugging Face: {repo_url}")
        
        # Aggiungi un file di esempio per verificare il deploy
        try:
            with open("huggingface_deploy.txt", "w") as f:
                f.write(f"Deployed from GitHub Actions\nRepository: {repo_name}\n")
            
            api.upload_file(
                repo_id=repo_id,
                path_in_repo="deploy_info.txt",
                path_or_fileobj="huggingface_deploy.txt"
            )
            print("✅ File di verifica caricato")
            
            # Pulizia
            if os.path.exists("huggingface_deploy.txt"):
                os.remove("huggingface_deploy.txt")
                
        except Exception as file_error:
            print(f"⚠️  Nota: Impossibile caricare file aggiuntivi: {file_error}")
        
        print("🎉 Deploy su Hugging Face completato con successo!")
        
    except Exception as e:
        print(f"❌ Errore durante il deploy su Hugging Face: {e}")
        # Non uscire con errore per non bloccare il deploy su Railway
        print("⚠️  Continuando con il workflow...")

if __name__ == "__main__":
    deploy_to_huggingface()