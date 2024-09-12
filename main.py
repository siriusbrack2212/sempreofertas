from flask import Flask, render_template
import requests

app = Flask(__name__)

# Configurações do Airtable
AIRTABLE_BASE_ID = 'appNwO27axKgEb6w7'  # ID da base do Airtable
AIRTABLE_TABLE_NAME = 'Products'         # Nome da tabela do Airtable
AIRTABLE_API_KEY = 'pat2QwwpmKHkee7GL.c28ad5f7dddda86a63b8aa20ed404d454f399cea45a0d08becf8e1f14a7d861c'  # Token de acesso pessoal

# URL da API do Airtable
AIRTABLE_API_URL = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

# Cabeçalhos para autenticação e tipo de conteúdo
HEADERS = {
    'Authorization': f'Bearer {AIRTABLE_API_KEY}',
    'Content-Type': 'application/json'
}

@app.route('/')
def index():
    try:
        response = requests.get(AIRTABLE_API_URL, headers=HEADERS)
        response.raise_for_status()  # Lança uma exceção para códigos de erro HTTP
        data = response.json()
        products = data.get('records', [])
        return render_template('home.html', products=products)
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Request failed: {e}")
        return "Failed to fetch data from Airtable", 500

if __name__ == '__main__':
    app.run(debug=True)


