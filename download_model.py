import os
import requests
from config import CLASSIFICATION_MODEL_FILENAME

MODEL_URL = os.environ.get("MODEL_URL")
MODELS_DIR = "models"
CLASSIFICATION_MODEL_PATH = os.path.join(MODELS_DIR, CLASSIFICATION_MODEL_FILENAME)

def main():
    if not MODEL_URL:
        print("[download_model] MODEL_URL no está definida. No se descargará el modelo.")
        return

    os.makedirs(MODELS_DIR, exist_ok=True)

    if os.path.exists(CLASSIFICATION_MODEL_PATH):
        print(f"[download_model] El modelo ya existe en {CLASSIFICATION_MODEL_PATH}, no se descarga de nuevo.")
        return

    print(f"[download_model] Descargando modelo desde {MODEL_URL}...")
    resp = requests.get(MODEL_URL, stream=True)
    resp.raise_for_status()

    with open(CLASSIFICATION_MODEL_PATH, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f"[download_model] Modelo descargado en {CLASSIFICATION_MODEL_PATH}")

if __name__ == "__main__":
    main()
