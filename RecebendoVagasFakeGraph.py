import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker

# Inicializando o fake para obter informações daqui do BR
fake = Faker('pt_BR')  # Configurar para gerar dados no formato brasileiro

# Lista reduzida de 10 cidades brasileiras
cities_brazil = [
    "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Salvador",
    "Brasília", "Curitiba", "Fortaleza", "Recife", "Manaus"
]

# Inicializando a lista vazia que receberá as vagas
vacancies = []

# Configurando a quantidade de dados
num_vacancies = 100

for _ in range(num_vacancies):
    vacancy_info = {
        "ID": fake.random_int(min=1, max=1000),
        "City": fake.random.choice(cities_brazil),  # Setando as cidades com base nas do brasil para ficar mais
                                                    # perto da nossa realidade.
        "Description": fake.text(max_nb_chars=200),
        "Status": fake.random_element(elements=("1 - PendingPublication", "2 - Published",
                                                "3 - Deactivated", "5 - Requested",
                                                "6 - Assigned", "7 - Expired")),
        "Published Date": fake.date_this_year(),
        "Number of Vacancies": fake.random_int(min=1, max=10)
    }
    vacancies.append(vacancy_info)

# Criar um DataFrame a partir da lista de vagas
df = pd.DataFrame(vacancies)

# Salvar o DataFrame em um arquivo Excel
df.to_excel("fake_vacancies_brazil_10_cities.xlsx", index=False)

print("Dados salvos em fake_vacancies_brazil_10_cities.xlsx")

# Plotar dados para análise
# Gráfico de barras: Número de vagas por cidade
city_counts = df['City'].value_counts()
city_counts.plot(kind='bar', figsize=(10, 6), title='Número de Vagas por Cidade no Brasil')
plt.xlabel('Cidade')
plt.ylabel('Número de Vagas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('fake_vagas_por_cidade_brazil_10_cities.png')
plt.show()

# Gráfico de pizza: Distribuição de Status das Vagas
status_counts = df['Status'].value_counts()
status_counts.plot(kind='pie', figsize=(8, 8), title='Distribuição de Status das Vagas', autopct='%1.1f%%')
plt.ylabel('')
plt.savefig('fake_distribuicao_status_vagas_brazil_10_cities.png')
plt.show()

# Gráfico de linha: Vagas publicadas ao longo do tempo
df['Published Date'] = pd.to_datetime(df['Published Date'])
df.set_index('Published Date', inplace=True)
df.resample('M').size().plot(kind='line', figsize=(10, 6), title='Vagas Publicadas ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Número de Vagas Publicadas')
plt.tight_layout()
plt.savefig('fake_vagas_publicadas_tempo_brazil_10_cities.png')
plt.show()
