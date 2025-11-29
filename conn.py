import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv() 

CREDENTIALS_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH")
DATABASE_URL = os.getenv("FIREBASE_DATABASE_URL")

def conectar_firebase():
    if not CREDENTIALS_PATH:
        print("ERRO: FIREBASE_CREDENTIALS_PATH não configurado no .env")
        return None

    try:
        if not firebase_admin._apps:
            cred = credentials.Certificate(CREDENTIALS_PATH)
            firebase_admin.initialize_app(cred, {
                'databaseURL': DATABASE_URL
            })
        
        return firestore.client()
        
    except Exception as e:
        print(f"ERRO ao conectar ao Firebase: {e}")
        return None

db = conectar_firebase()