from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

app = Flask(__name__)

# Configurações do Airtable
AIRTABLE_BASE_ID = 'appNwO27axKgEb6w7'  # ID da base do Airtable
PRODUCTS_TABLE_NAME = 'Products'         # Nome da tabela de produtos
VOTES_TABLE_NAME = 'vote'               # Nome da tabela de votos
AIRTABLE_API_KEY = 'pat2QwwpmKHkee7GL.c28ad5f7dddda86a63b8aa20ed404d454f399cea45a0d08becf8e1f14a7d861c'  # Token de acesso pessoal

# URLs da API do Airtable
PRODUCTS_API_URL = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{PRODUCTS_TABLE_NAME}'
VOTES_API_URL = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{VOTES_TABLE_NAME}'

# Cabeçalhos para autenticação e tipo de conteúdo
HEADERS = {
    'Authorization': f'Bearer {AIRTABLE_API_KEY}',
    'Content-Type': 'application/json'
}

@app.route('/')
def index():
    response = requests.get(PRODUCTS_API_URL, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        products = data.get('records', [])
        return render_template('home.html', products=products)
    else:
        return jsonify({'error': 'Failed to fetch data from Airtable'}), response.status_code

@app.route('/vote', methods=['POST'])
def vote():
    product_id = request.form.get('product_id')
    name = request.form.get('name')

    if not product_id or not name:
        return jsonify({'error': 'Missing product_id or name'}), 400

    # Dados a serem inseridos na tabela "Votes"
    vote_data = {
        "fields": {
            "Product": [product_id],  # Referência ao produto que foi votado
            "Name": name              # Nome da pessoa que votou
        }
    }

    # Enviando a requisição POST para criar um novo registro de voto
    response = requests.post(VOTES_API_URL, headers=HEADERS, json=vote_data)

    if response.status_code == 200:
        return redirect(url_for('index'))  # Redireciona para a página inicial após a votação
    else:
        return jsonify({'error': f'Failed to save vote in Airtable: {response.json()}'})

if __name__ == '__main__':
    app.run(debug=True)



