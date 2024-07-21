import pandas as pd

import requests
#Import usado para fazer requisições HTTP

# Chamando a API do pandape, passando o endpoint junto na URL.
base_url = "https://api.pandape.com.br/v2/vacancies"

# Parâmetros da requisição
params = {
    "VacancyStatus": 2,
    "VacancyType": 3,
    "Page": 1,
    "PageSize": 10
}

# TOKEN DA API
headers = {
    "Authorization": "Bearer TOKEN"  #
}

# Fazendo a requisição com o método GET para passando como parâmetro o token e os parametros
response = requests.get(base_url, headers=headers, params=params)

# Verificando o status da requisição  e convertendo para um json
if response.status_code == 200:

    data = response.json()

    #inicializando uma lista vazia no nosso escopo para receber dados de um append
    vacancies = []

    # usando um laço for para percorrer uma lista com nossas informações e fazer um append na nossa lista vazia

    for vacancy in data['Items']:
        vacancy_info = {
            "ID": vacancy['IdVacancy'],
            "City": vacancy['City'],
            "Description": vacancy['Description'],
            "Status": vacancy['Status'],
            "Published Date": vacancy['PublishedDate'],
            "Number of Vacancies": vacancy['NumberVacancies']
        }
        vacancies.append(vacancy_info)

    # usando o pandas e o dataframe para enchergar a minha lista e entender que se trata de algo bidimensional.
    df = pd.DataFrame(vacancies)

    # Salvar o DataFrame em um arquivo Excel
    df.to_excel("vacancies.xlsx", index=False)

    print("Dados salvos em vacancies.xlsx")
else:
    print(f"Erro na requisição: {response.status_code}")