import requests

# URL para obter o token
token_url = "https://login.pandape.com.br/connect/token"

# Credenciais do cliente
client_id = "23212311"
client_secret = "12234"

# Parâmetros da requisição
payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'PandapeApi'
}

# Cabeçalhos
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Fazendo a requisição POST para obter o token
response = requests.post(token_url, data=payload, headers=headers)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    token = response.json().get('access_token')
    print(f"Token: {token}")
else:
    print(f"Falha ao obter o token: {response.status_code}")
    print(response.json())
