import requests
from bs4 import BeautifulSoup

# URL do site que você quer fazer o scraping
url = "https://www.dafiti.com.br/roupas-masculinas/camisas/"

# Fazendo a requisição HTTP para obter o conteúdo da página
response = requests.get(url)
content = response.text

# Usando BeautifulSoup para analisar o HTML
soup = BeautifulSoup(content, 'html.parser')

# Encontrando todos os itens de camisa na página
camisas = soup.find_all('div', class_='product-box-detail')

# Iterando sobre as camisas encontradas e extraindo o nome e preço
for camisa in camisas:
    nome_tag = camisa.find('p', class_='product-box-title')
    preco_tag = camisa.find('span', class_='product-box-price-to')

    if nome_tag and preco_tag:
        nome = nome_tag.get_text(strip=True)
        preco = preco_tag.get_text(strip=True)
        print(f"Nome: {nome}, Preço: {preco}")
    else:
        print("Elemento não encontrado ou estrutura HTML mudou.")
