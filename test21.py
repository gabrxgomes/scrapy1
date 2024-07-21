import requests
import json

# URL do endpoint da API
url = "https://api.pandape.com.br/v2/vacancies"

# Cabeçalhos com autenticação (substitua 'YOUR_API_TOKEN' pelo token real)
headers = {
    "Authorization": "https://login.pandape.com.br/connect/token"
}

# Fazendo a requisição GET para o endpoint
response = requests.get(url, headers=headers)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    vacancies = response.json()
    # Processar e transformar os dados conforme necessário
    # Por exemplo, filtrando, agregando ou formatando os dados para o PowerBI
    print(json.dumps(vacancies, indent=4))
else:
    print(f"Falha na requisição: {response.status_code}")
