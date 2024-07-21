import requests
import json

# Função para obter as informações da vaga com base no idRequest
def get_vacancy_info(token, idRequest):
    # URL da API do PandaPé para obter as informações da vaga
    base_url = f"https://api.pandape.com.br/v2/vacancies/{idRequest}"

    # Cabeçalho de autenticação
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json" #expecificando o tipo do arquivo
    }

    # Fazer a requisição GET
    response = requests.get(base_url, headers=headers)

    # Verificar o status da resposta
    if response.status_code == 200:
        # Converter a resposta para JSON
        data = response.json()
        print("Informações da vaga:")
        print(json.dumps(data, indent=4, ensure_ascii=False))
    else:
        print(f"Erro ao obter informações da vaga: {response.status_code}")
        print(response.text)

# Variável de autenticação
token = "YOUR_ACCESS_TOKEN"

# ID da requisição da vaga
idRequest = 12345  # Substitua pelo ID da requisição real

# Obter as informações da vaga passo o token junto com o idrequest
get_vacancy_info(token, idRequest)



