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
    'PublishedDate': [fake.date_this_year() for _ in range(num_vacancies)]
}

df = pd.DataFrame(data)

# Calcular KPIs

# Contagem de vagas por status
status_counts = df['VacancyStatus'].value_counts().sort_index()
status_labels = {
    1: 'PendingPublication',
    2: 'Published',
    3: 'Deactivated',
    5: 'Requested',
    6: 'Assigned',
    7: 'Expired'
}
status_counts.index = status_counts.index.map(status_labels)

# Contagem de vagas por tipo
type_counts = df['VacancyType'].value_counts().sort_index()
type_labels = {
    1: 'InternalRecruitment',
    2: 'Confidential',
    3: 'Public'
}
type_counts.index = type_counts.index.map(type_labels)

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
