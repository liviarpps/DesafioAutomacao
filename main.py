from supabase import create_client
from dotenv import load_dotenv

import requests
import os

load_dotenv()

INSTANCE = os.getenv("ZAPI_INSTANCE")
TOKEN= os.getenv("ZAPI_TOKEN")
CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN", "")

supabase= create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY"),
)

response = (
    supabase
    .table("contatos")
    .select("nome, telefone")
    .limit(3)
    .execute()
)

contatos = response.data
print(f"contatos: {len(contatos)}")
print(contatos)

for contato in contatos:
    nome = contato.get("nome", "").strip()
    telefone = contato.get("telefone", "")

    if not nome or not telefone:
        print(f"Contato inválido")
        continue

    mensagem = f"Olá, {nome} tudo bem com você?"

    headers = {"Content-Type": "application/json"}
    if CLIENT_TOKEN:
        headers["Client-Token"] = CLIENT_TOKEN
    
    try:     
        resposta = requests.post(
        f"https://api.z-api.io/instances/{INSTANCE}/token/{TOKEN}/send-text",json={
            "phone": telefone,
            "message": mensagem,
        },

        headers=headers,
        timeout=30,
        )
        resposta.raise_for_status()
        print(f"Mensagem para {nome}")

    except Exception as erro:
        print(f"Erro ao enviar mensagem para {nome}: {erro}")