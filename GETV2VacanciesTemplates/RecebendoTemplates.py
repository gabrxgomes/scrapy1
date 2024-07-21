import requests
import json

# Função para obter a lista de modelos de vagas
def get_vacancy_templates(token):
    # URL da API do PandaPé para obter a lista de modelos de vagas
    base_url = "https://api.pandape.com.br/v2/vacancies/templates"

    # Cabeçalho de autenticação
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "accept": "application/json"
    }

    # Fazer a requisição GET
    response = requests.get(base_url, headers=headers)

    # Verificar o status da resposta
    if response.status_code == 200:
        # Converter a resposta para JSON
        data = response.json()
        print("Lista de modelos de vagas:")
        print(json.dumps(data, indent=4, ensure_ascii=False))
    else:
        print(f"Erro ao obter a lista de modelos de vagas: {response.status_code}")
        print(response.text)

# Variável de autenticação
token = "YOUR_ACCESS_TOKEN"

# Obter a lista de modelos de vagas
get_vacancy_templates(token)
