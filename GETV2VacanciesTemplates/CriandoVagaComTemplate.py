import requests
import json


def create_vacancy_with_template(token, id_template):
    # URL da API do PandaPé para criar uma nova vaga
    base_url = "https://api.pandape.com.br/v2/vacancies"

    # Dados da nova vaga, utilizando o template
    new_vacancy_data = {
        "IdUser": 123,  # ID do usuário responsável
        "IdRequestToAssociate": 456,  # ID de uma solicitação a ser associada, se aplicável
        "Reference": "Ref-001",
        "Job": "Desenvolvedor Python",
        "JobComplement": "Backend",
        "IdCategory1": 1,
        "IdCategory2": 2,
        "IdLocation1": 1,
        "IdLocation2": 2,
        "IdLocation3": 3,
        "IdManagerialLevel": 1,
        "Description": ("Estamos em busca de um Desenvolvedor Python para se juntar à nossa equipe. "
                        "O candidato ideal deve ter experiência com desenvolvimento em Python, conhecimento "
                        "em bancos de dados relacionais, e habilidades em resolução de problemas. "
                        "O trabalho inclui manutenção e desenvolvimento de novos módulos no sistema "
                        "existente, além de colaborar com a equipe de TI para melhorias contínuas. "
                        "É necessário ter uma boa comunicação e ser capaz de trabalhar em equipe."),
        "NumberVacancies": 1,
        "IdContractWorkType": 1,
        "IdWorkingHours": 1,
        "IdWorkMethod": 1,
        "SalaryMin": "3000",
        "SalaryMax": "5000",
        "HideSalary": False,
        "CEP": "01000-000",
        "VacancyLocationType": "0 - CompanyAddress",
        "CompanyHidden": False,
        "AlternativeDescription": "Procuramos um Desenvolvedor Python com experiência em backend.",
        "YoutubeVideoUrl": "",
        "IdStudy1Min": 1,
        "CompanyHiddenName": "",
        "ContractDate": "2024-07-20T18:06:10.115Z",
        "IdExperienceRange": 1,
        "AgeMin": 25,
        "AgeMax": 40,
        "IdSex": 0,
        "DeficiencyRequired": False,
        "DeficiencyInformation": "",
        "CIDRequired": False,
        "Deficiencies": [],
        "ChangeResidenceAvailabilityRequired": False,
        "TravelAvailabilityRequired": False,
        "VehicleRequired": False,
        "LicenseRequired": False,
        "IdLicenseList": [],
        "Studies": [
            {
                "IdStudy1": 1,
                "IdStudy2": 2
            }
        ],
        "Languages": [
            {
                "IdLanguage": 1,
                "IdLanguageLevel": 1
            }
        ],
        "Benefits": [
            "Vale Refeição", "Vale Transporte"
        ],
        "Skills": [
            "Python", "Django", "SQL"
        ],
        "Tags": [
            "Backend", "Desenvolvedor"
        ],
        "Publish": True,
        "IsDeficiencyHidden": False
    }

    # Cabeçalho de autenticação
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Fazer a requisição POST
    response = requests.post(base_url, headers=headers, json=new_vacancy_data)

    # Verificar o status da resposta
    if response.status_code == 201:
        print("Vaga criada com sucesso!")
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print(f"Erro ao criar a vaga: {response.status_code}")
        print(response.text)


# Variável de autenticação
token = "YOUR_ACCESS_TOKEN"

# ID do template a ser utilizado
id_template = 1

# Criar uma nova vaga utilizando o template
create_vacancy_with_template(token, id_template)
