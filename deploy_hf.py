from huggingface_hub import HfApi, upload_folder
import os

def deploy_to_hf():
    api = HfApi()
    
    # Upload dei file del modello (modifica i path secondo le tue esigenze)
    upload_folder(
        folder_path="./model",  # o la cartella del tuo modello
        repo_id="tuo-username/tuo-nome-modello",
        commit_message="Auto-deploy from CI"
    )
    
    print("Deploy su Hugging Face completato!")

if __name__ == "__main__":
    deploy_to_hf()