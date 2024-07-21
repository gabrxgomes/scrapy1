import requests
import json



def get_vacancy_template_details(token, idVacancyTemplate):
    # URL para obter detalhes do modelo de vaga específico
    template_details_url = f"https://api.pandape.com.br/v2/vacancies/templates/{idVacancyTemplate}"

    # Cabeçalho de autenticação
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Fazer a requisição GET para obter os detalhes do modelo de vaga específico
    response = requests.get(template_details_url, headers=headers)

    # Verificar o status da resposta
    if response.status_code == 200:
        template_details = response.json()
        print("Detalhes do modelo de vaga:")
        print(json.dumps(template_details, indent=4, ensure_ascii=False))
        return template_details
    else:
        print(f"Erro ao obter detalhes do modelo de vaga: {response.status_code}")
        print(response.text)
        return None


# Variável de autenticação
token = "YOUR_ACCESS_TOKEN"

# ID do modelo de vaga que você deseja obter detalhes
idVacancyTemplate = 1  # Substitua pelo ID real do modelo de vaga

# Obter detalhes do modelo de vaga específico
get_vacancy_template_details(token, idVacancyTemplate)
