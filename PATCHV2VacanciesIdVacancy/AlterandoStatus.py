import requests
import json


# Função para alterar o status de uma vaga
def update_vacancy_status(token, idVacancy, new_status):
    # URL para alterar o status da vaga
    update_url = f"https://api.pandape.com.br/v2/vacancies/{idVacancy}"

    # Cabeçalho de autenticação
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Dados para alterar o status da vaga
    payload = {
        "Status": new_status
    }

    # Fazer a requisição PATCH para alterar o status da vaga
    response = requests.patch(update_url, headers=headers, json=payload)

    # Verificar o status da resposta
    if response.status_code == 200:
        print("Status da vaga atualizado com sucesso.")
    else:
        print(f"Erro ao atualizar o status da vaga: {response.status_code}")
        print(response.text)


# Variável de autenticação (substitua pelo seu token real)
token = "YOUR_ACCESS_TOKEN"

# ID da vaga que você deseja atualizar (substitua pelo ID real da vaga)
idVacancy = 12345  # Exemplo de ID

# Novo status da vaga (substitua pelo status desejado)
new_status = 3  # Exemplo: 3 - Deactivated

# Alterar o status da vaga
update_vacancy_status(token, idVacancy, new_status)
