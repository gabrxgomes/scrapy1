import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker

# Inicializar o gerador de dados falsos
fake = Faker()

# Número de vagas para gerar
num_vacancies = 1000

# Gerar dados falsos
data = {
    'IdVacancy': range(1, num_vacancies + 1),
    'VacancyStatus': np.random.choice([1, 2, 3, 5, 6, 7], size=num_vacancies),
    'VacancyType': np.random.choice([1, 2, 3], size=num_vacancies),
    'City': [fake.city() for _ in range(num_vacancies)],
    'PublishedDate': [fake.date_this_year() for _ in range(num_vacancies)],
    'IdWorkMethod': np.random.choice([1, 2, 3], size=num_vacancies)
}

df = pd.DataFrame(data)

# Mapeamento de rótulos
status_labels = {
    1: 'PendingPublication',
    2: 'Published',
    3: 'Deactivated',
    5: 'Requested',
    6: 'Assigned',
    7: 'Expired'
}

type_labels = {
    1: 'InternalRecruitment',
    2: 'Confidential',
    3: 'Public'
}

work_method_labels = {
    1: 'Remote',
    2: 'On-site',
    3: 'Hybrid'
}

# Calcular KPIs

# Contagem de vagas por status
status_counts = df['VacancyStatus'].value_counts().sort_index()
status_counts.index = status_counts.index.map(status_labels)

# Contagem de vagas por tipo
type_counts = df['VacancyType'].value_counts().sort_index()
type_counts.index = type_counts.index.map(type_labels)

# Contagem de vagas por método de trabalho
work_method_counts = df['IdWorkMethod'].value_counts().sort_index()
work_method_counts.index = work_method_counts.index.map(work_method_labels)

# Distribuição das vagas por cidade (as 10 cidades mais comuns)
city_counts = df['City'].value_counts().head(10)

# Distribuição de vagas ao longo do tempo (datas de publicação)
df['PublishedDate'] = pd.to_datetime(df['PublishedDate'])
date_counts = df['PublishedDate'].value_counts().sort_index()

# Visualizar KPIs

# Configurações do gráfico
sns.set(style="whitegrid")

# Gráfico de contagem de vagas por status
plt.figure(figsize=(12, 6))
sns.barplot(x=status_counts.index, y=status_counts.values, palette="viridis")
plt.title('Contagem de Vagas por Status')
plt.xlabel('Status da Vaga')
plt.ylabel('Número de Vagas')
plt.xticks(rotation=45)
plt.show()

# Gráfico de contagem de vagas por tipo
plt.figure(figsize=(12, 6))
sns.barplot(x=type_counts.index, y=type_counts.values, palette="coolwarm")
plt.title('Contagem de Vagas por Tipo')
plt.xlabel('Tipo da Vaga')
plt.ylabel('Número de Vagas')
plt.xticks(rotation=45)
plt.show()

# Gráfico de contagem de vagas por método de trabalho
plt.figure(figsize=(12, 6))
sns.barplot(x=work_method_counts.index, y=work_method_counts.values, palette="plasma")
plt.title('Contagem de Vagas por Método de Trabalho')
plt.xlabel('Método de Trabalho')
plt.ylabel('Número de Vagas')
plt.xticks(rotation=45)
plt.show()

# Gráfico de contagem de vagas por cidade
plt.figure(figsize=(12, 6))
sns.barplot(x=city_counts.index, y=city_counts.values, palette="magma")
plt.title('Contagem de Vagas por Cidade (Top 10)')
plt.xlabel('Cidade')
plt.ylabel('Número de Vagas')
plt.xticks(rotation=45)
plt.show()

# Gráfico de distribuição de vagas ao longo do tempo
plt.figure(figsize=(12, 6))
sns.lineplot(x=date_counts.index, y=date_counts.values)
plt.title('Distribuição de Vagas ao Longo do Tempo')
plt.xlabel('Data de Publicação')
plt.ylabel('Número de Vagas')
plt.xticks(rotation=45)
plt.show()
