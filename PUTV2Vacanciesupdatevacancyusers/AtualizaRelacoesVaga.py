import requests
import json


# Função para atualizar os usuários associados a uma vaga
def update_vacancy_users(api_key, token, id_vacancy, id_company_user_action, ids_company_users):
    # URL para atualizar os usuários associados a uma vaga
    update_url = "https://api.pandape.com.br/v2/vacancies/updatevacancyusers"

    # Cabeçalho de autenticação
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Corpo da requisição
    payload = {
        "IdVacancy": id_vacancy,
        "IdCompanyUserAction": id_company_user_action,
        "IdsCompanyUsers": ids_company_users
    }

    # Fazer a requisição PUT para atualizar os usuários associados à vaga
    response = requests.put(update_url, headers=headers, json=payload)

    # Verificar o status da resposta
    if response.status_code == 200:
        print("Usuários associados à vaga atualizados com sucesso.")
    else:
        print(f"Erro ao atualizar os usuários associados à vaga: {response.status_code}")
        print(response.text)


# Variáveis de autenticação (substitua pelos valores reais)
token = "YOUR_ACCESS_TOKEN"

# Dados da requisição (substitua pelos valores reais)
id_vacancy = 12345  # Exemplo de ID da vaga
id_company_user_action = 67890  # Exemplo de ID do usuário da empresa que realiza a ação
ids_company_users = [11111, 22222, 33333]  # Exemplo de IDs de usuários da empresa a serem associados à vaga

# Atualizar os usuários associados à vaga
update_vacancy_users(token, id_vacancy, id_company_user_action, ids_company_users)
