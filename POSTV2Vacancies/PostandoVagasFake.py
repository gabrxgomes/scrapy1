import requests
from faker import Faker
import json

# Inicializando o faker para obter informações fake
fake = Faker('pt_BR')

# Função para gerar dados fake para uma vaga
def generate_fake_vacancy():
    return {
        "IdUser": fake.random_int(min=1, max=1000),
        "IdRequestToAssociate": fake.random_int(min=1, max=1000),
        "Reference": fake.bothify(text='REF-####'),
        #"Job": fake.job(),  definindo um valor dinâmico com o fake
        "Job": "Desenvolvedor Delphy",  # Definindo um valor estático
        "JobComplement": fake.bs(),
        "IdCategory1": fake.random_int(min=1, max=10),
        "IdCategory2": fake.random_int(min=1, max=10),
        "IdLocation1": fake.random_int(min=1, max=10),
        "IdLocation2": fake.random_int(min=1, max=10),
        "IdLocation3": fake.random_int(min=1, max=10),
        "IdManagerialLevel": fake.random_int(min=1, max=10),
        #"Description": fake.text(max_nb_chars=200), - vaga com valor dinâmico

        "Description": ("Estamos em busca de um Desenvolvedor Delphy para se juntar à nossa equipe. "
                        "O candidato ideal deve ter experiência com desenvolvimento em Delphy, conhecimento"
                        " em bancos de dados relacionais, e habilidades em resolução de problemas. "
                        "O trabalho inclui manutenção e desenvolvimento de novos módulos no sistema "
                        "existente, além de colaborar com a equipe de TI para melhorias contínuas. "
                        "É necessário ter uma boa comunicação e ser capaz de trabalhar em equipe."), # vaga com valor fixo

        "NumberVacancies": fake.random_int(min=1, max=10),
        "IdContractWorkType": fake.random_int(min=1, max=10),
        "IdWorkingHours": fake.random_int(min=1, max=10),
        "IdWorkMethod": fake.random_int(min=1, max=10),
        "SalaryMin": fake.pricetag(),  # Salário mínimo
        "SalaryMax": fake.pricetag(),  # Salário máximo
        "HideSalary": fake.boolean(),  # Ocultar salário
        "CEP": fake.postcode(),        # CEP (Código Postal)
        "VacancyLocationType": "0 - CompanyAddress",
        "CompanyHidden": fake.boolean(),  # Empresa oculta
        #"AlternativeDescription": fake.text(max_nb_chars=200),
        "AlternativeDescription": (
            "Procura-se Desenvolvedor Delphy experiente para atuar em manutenção e criação de módulos em nosso sistema. "
            "Ideal para quem tem forte conhecimento em Delphy e bancos de dados relacionais."
        ),
        
        #"YoutubeVideoUrl": fake.url(),  # URL do vídeo no youtube
        "YoutubeVideoUrl": "https://youtube.com/video_resume",
        "IdStudy1Min": fake.random_int(min=1, max=10),
        "CompanyHiddenName": fake.company(),
        "ContractDate": fake.date_this_year().isoformat(),  # Data do contrato
        "IdExperienceRange": fake.random_int(min=1, max=10),
        #"AgeMin": fake.random_int(min=18, max=60),
        "AgeMin": 18,
        #"AgeMax": fake.random_int(min=18, max=60),
        "AgeMax": 60,
        "IdSex": fake.random_int(min=1, max=2),  # 1 para masculino, 2 para feminino
        "DeficiencyRequired": fake.boolean(),  # Deficiência requerida
        #"DeficiencyInformation": fake.text(max_nb_chars=100),
        "DeficiencyInformation": "A vaga é inclusiva e está aberta a candidatos com deficiências. Valorizamos a diversidade e incentivamos pessoas com deficiência a se candidatarem. "
                                 "Adaptaremos o ambiente de trabalho para atender às necessidades específicas e garantiremos que todos os candidatos recebam as acomodações necessárias "
                                 "durante o processo de seleção e ao longo de seu tempo conosco.",

        "CIDRequired": fake.boolean(),  # CID necessário
        "Deficiencies": [  # Lista de deficiências
            {
                "IdDeficiency1": fake.random_int(min=1, max=10),
                "IdDeficiency2List": [fake.random_int(min=1, max=10) for _ in range(3)]
            }
        ],
        "ChangeResidenceAvailabilityRequired": fake.boolean(),
        "TravelAvailabilityRequired": fake.boolean(),
        "VehicleRequired": fake.boolean(),
        "LicenseRequired": fake.boolean(),
        "IdLicenseList": [fake.random_int(min=1, max=10) for _ in range(2)],
        "Studies": [  # Lista de estudos
            {
                "IdStudy1": fake.random_int(min=1, max=10),
                "IdStudy2": fake.random_int(min=1, max=10)
            }
        ],
        "Languages": [  # Lista de idiomas
            {
                "IdLanguage": fake.random_int(min=1, max=10),
                "IdLanguageLevel": fake.random_int(min=1, max=5)
            }
        ],
        "Benefits": [fake.word() for _ in range(3)],
        "Skills": [fake.word() for _ in range(3)],
        "Tags": [fake.word() for _ in range(3)],
        "Publish": fake.boolean(),  # Publicar vaga
        "IsDeficiencyHidden": fake.boolean()  # Deficiência oculta
    }

# Gerar dados fake para uma vaga
fake_vacancy = generate_fake_vacancy()

# Converter os dados para JSON
fake_vacancy_json = json.dumps(fake_vacancy, indent=4, ensure_ascii=False)


print("Dados gerados para envio:\n", fake_vacancy_json)

# Simulando o envio da requisição POST
base_url = "https://api.pandape.com.br/v2/vacancies"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

# Enviar a requisição POST (comente a linha abaixo se não deseja realizar a requisição real)
response = requests.post(base_url, headers=headers, data=fake_vacancy_json)

# Verificar o status da resposta
if response.status_code == 201:
    print("Vaga criada com sucesso!")
else:
    print(f"Erro ao criar vaga: {response.status_code}")
