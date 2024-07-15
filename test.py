import requests
from bs4 import BeautifulSoup
import re

#PESQUISA DE PELAVRAS CHAVE NA PÁGINA

# URL do site que você quer fazer o scraping
url = "https://www.dafiti.com.br/roupas-masculinas/camisas/"  # substitua pelo URL desejado

# Fazendo a requisição HTTP para obter o conteúdo da página
response = requests.get(url)
content = response.text

# Usando BeautifulSoup para analisar o HTML
soup = BeautifulSoup(content, 'html.parser')
text = soup.get_text()

# Usando a expressão regular para buscar a palavra "camisa"
resultados = re.findall(r"camisas", text, re.IGNORECASE)

# Exibindo os resultados
print(f"Encontramos {len(resultados)} ocorrências da palavra 'camisas'.")
for resultado in resultados:
    print(resultado)
