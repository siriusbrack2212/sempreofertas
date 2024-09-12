from flask import Flask, jsonify
import requests


app = Flask(__name__)

# Configurações do Airtable
AIRTABLE_BASE_ID = 'appNwO27axKgEb6w7'  # Substitua com o ID da sua base
AIRTABLE_TABLE_NAME = 'Products'         # Substitua com o nome da sua tabela
AIRTABLE_API_KEY = 'pat2QwwpmKHkee7GL.c28ad5f7dddda86a63b8aa20ed404d454f399cea45a0d08becf8e1f14a7d861c'  # Substitua com o seu token de acesso pessoal

# URL da API do Airtable
AIRTABLE_API_URL = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

# Cabeçalhos para autenticação e tipo de conteúdo
HEADERS = {
    'Authorization': f'Bearer {AIRTABLE_API_KEY}',
    'Content-Type': 'application/json'
}

@app.route('/')
def index():
    response = requests.get(AIRTABLE_API_URL, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)  # Retorna os dados em formato JSON
    else:
        return jsonify({'error': 'Failed to fetch data from Airtable'}), response.status_code



