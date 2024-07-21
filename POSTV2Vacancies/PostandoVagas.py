import requests
import json

# URL da API do PandaPé para criar uma nova vaga pelo endpoint
base_url = "https://api.pandape.com.br/v2/vacancies"

# Dados da vaga a serem cadastrados via metodo http - POST
vacancy_data = {
    "IdUser": 123,  # ID do usuário que está criando a vaga
    "IdRequestToAssociate": 456,  # ID da requisição para associar (se aplicável)
    "Reference": "REF1234",  # Referência da vaga
    "Job": "Desenvolvedor Delphi",  # Cargo da vaga
    "JobComplement": "Senior",  # Complemento do cargo no nosso caso a "senioridade"
    "IdCategory1": 1,  # ID da categoria principal
    "IdCategory2": 2,  # ID da subcategoria
    "IdLocation1": 3,  # ID da localização principal
    "IdLocation2": 4,  # ID da localização secundária
    "IdLocation3": 5,  # ID da localização terciária
    "IdManagerialLevel": 6,  # ID do nível de gerência
    "Description": ("Estamos em busca de um Desenvolvedor Delphi para se juntar à nossa equipe. "
                    "O candidato ideal deve ter experiência com desenvolvimento em Delphi, conhecimento "
                    "em bancos de dados relacionais, e habilidades em resolução de problemas. "
                    "O trabalho inclui manutenção e desenvolvimento de novos módulos no sistema "
                    "existente, além de colaborar com a equipe de TI para melhorias contínuas. "
                    "É necessário ter uma boa comunicação e ser capaz de trabalhar em equipe."), # Descrição da vaga
    "NumberVacancies": 3,  # Número de vagas disponíveis
    "IdContractWorkType": 7,  # ID do tipo de contrato de trabalho
    "IdWorkingHours": 8,  # ID do tipo de carga horária
    "IdWorkMethod": 9,  # ID do método de trabalho
    "SalaryMin": "R$ 10.000",  # Salário mínimo
    "SalaryMax": "R$ 15.000",  # Salário máximo
    "HideSalary": False,  # Mostrar o salário
    "CEP": "01000-000",  # CEP da localização
    "VacancyLocationType": "0 - CompanyAddress",  # Tipo de localização
    "CompanyHidden": False,  # A empresa está oculta?
    "AlternativeDescription": "Desenvolvedor Delphi com foco em sistemas financeiros.",
    "YoutubeVideoUrl": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # URL do vídeo
    "IdStudy1Min": 4,  # ID do nível de estudo mínimo
    "CompanyHiddenName": "TechCorp",  # Nome oculto da empresa
    "ContractDate": "2024-07-20T20:56:03.394Z",  # Data do contrato
    "IdExperienceRange": 5,  # ID da faixa de experiência
    "AgeMin": 25,  # Idade mínima
    "AgeMax": 45,  # Idade máxima
    "IdSex": 1,  # ID do sexo (1 para masculino, 2 para feminino, etc.)
    "DeficiencyRequired": True,  # Deficiência requerida
    "DeficiencyInformation": "Experiência em ambientes diversos e inclusivos.", # Informação sobre a vaga para
    # deficiêntes
    "CIDRequired": True,  # CID (Classificação Internacional de Doenças) requerida
    "Deficiencies": [
        {
            "IdDeficiency1": 1,  # ID da deficiência principal
            "IdDeficiency2List": [2, 3]  # Lista de IDs de deficiências secundárias
        }
    ],
    "ChangeResidenceAvailabilityRequired": True,  # Disponibilidade para mudança de residência
    "TravelAvailabilityRequired": True,  # Disponibilidade para viagens
    "VehicleRequired": True,  # Veículo necessário
    "LicenseRequired": True,  # Licença necessária
    "IdLicenseList": [1],  # Lista de IDs de licenças necessárias
    "Studies": [
        {
            "IdStudy1": 1,  # ID do primeiro nível de estudo
            "IdStudy2": 2  # ID do segundo nível de estudo (opcional)
        }
    ],
    "Languages": [
        {
            "IdLanguage": 1,  # ID do idioma
            "IdLanguageLevel": 2  # Nível de proficiência no idioma
        }
    ],
    "Benefits": ["Vale Transporte", "Vale Alimentação", "Gympass", "Plano Odontológico", "Plano de Saúde"],  # Benefícios oferecidos
    "Skills": ["Programação em Delphi", "Banco de Dados Relacional", "Banco de dados não Relacional",
               "Microsserviços", "Mensageria"],  # Habilidades necessárias
    "Tags": ["Desenvolvimento", "TI", "Finanças", "Microsserviços"],  # Tags relacionadas
    "Publish": True,  # Publicar a vaga - OK
    "IsDeficiencyHidden": False  # Deficiência oculta? Autismo, TDAH, DOENÇA DE LYME
}

# TOKEN DA API
headers = {
    "Authorization": "Bearer SEU_TOKEN_AQUI",
    "Content-Type": "application/json"  # Definir o tipo de conteúdo como JSON, cada expecificação é um erro a menos.
}

# Fazer a requisição POST para criar uma nova vaga
response = requests.post(base_url, headers=headers, data=json.dumps(vacancy_data))

# Verificar o status da resposta
if response.status_code == 201:
    print("Vaga criada com sucesso!")
    response_data = response.json()
    id_request = response_data.get("IdRequest")  # Pegar o ID da requisição da resposta para usarmos na request "GET/v2/vacancies/{idRequest}"
    print(f"ID da requisição: {id_request}")
else:
    print(f"Erro ao criar a vaga: {response.status_code}")
    print(response.text)
