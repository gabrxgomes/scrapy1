import requests
import pandas as pd
import matplotlib.pyplot as plt

# URL da API
base_url = "https://api.pandape.com.br/v2/vacancies"

# Parâmetros da requisição
params = {
    "VacancyStatus": 2,
    "VacancyType": 3,
    "Page": 1,
    "PageSize": 10
}

# Token da API
headers = {
    "Authorization": "Bearer SEU_TOKEN_AQUI"  # Substitua SEU_TOKEN_AQUI pelo seu token de autenticação real
}

# Fazer a requisição GET
response = requests.get(base_url, params=params, headers=headers)

# Verificar o status da resposta
if response.status_code == 200:
    # Converter a resposta para JSON
    data = response.json()

    # Exibir os dados resultantes
    vacancies = []
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

    # Criar um DataFrame a partir da lista de vagas
    df = pd.DataFrame(vacancies)

    # Salvar o DataFrame em um arquivo Excel
    df.to_excel("vacancies_brazil.xlsx", index=False)

    print("Dados salvos em vacancies_brazil.xlsx")

    # Plotar dados para análise
    # Gráfico de barras: Número de vagas por cidade
    city_counts = df['City'].value_counts()
    city_counts.plot(kind='bar', figsize=(10, 6), title='Número de Vagas por Cidade no Brasil')
    plt.xlabel('Cidade')
    plt.ylabel('Número de Vagas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('vagas_por_cidade_brazil.png')
    plt.show()

    # Gráfico de pizza: Distribuição de Status das Vagas
    status_counts = df['Status'].value_counts()
    status_counts.plot(kind='pie', figsize=(8, 8), title='Distribuição de Status das Vagas', autopct='%1.1f%%')
    plt.ylabel('')
    plt.savefig('distribuicao_status_vagas_brazil.png')
    plt.show()

    # Gráfico de linha: Vagas publicadas ao longo do tempo
    df['Published Date'] = pd.to_datetime(df['Published Date'])
    df.set_index('Published Date', inplace=True)
    df.resample('M').size().plot(kind='line', figsize=(10, 6), title='Vagas Publicadas ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Número de Vagas Publicadas')
    plt.tight_layout()
    plt.savefig('vagas_publicadas_tempo_brazil.png')
    plt.show()

else:
    print(f"Erro na requisição: {response.status_code}")
