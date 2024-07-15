from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import openpyxl

options = webdriver.ChromeOptions() #cria opções para usar o webdriver no chrome
options.headless = True #o modo headles permite que possamos executar um script de automação
#ou de scraping em sites que estão rodando em produção em servidores linux, fora o aumento
#da performance e menos consumo de memoria do crawling
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
#o codigo a cima inicializa o driver do chrome com configurações especificas

#definindo uma variavel para o site alvo/pagina
url = 'https://www.kabum.com.br/computadores/notebooks/notebook-acer'

#navegando para o site alvo passado como parâmetro (url)
driver.get(url)

#instanciamos uma lista vazia para armazenar o que queremos buscar na pagina, no nosso caso produtos
items = []

#o last_height compreende onde a pagina começa em questão de altura, cada pagina por si só possui uma altura e uma
# largura onde os itens (divs e etc) começam a ser dispostos no layout, scraping é a varredura
# correta em um determinado layout!
last_height = driver.execute_script('return document.body.scrollHeight')


#define a quantidade alvo de informações a ser coletadas
itemTargetCount = 25



# INICIO DO SCROLLING ATÉ O FINAL DA PÁGINA
while itemTargetCount > len(items):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    # Wait for content to load
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')

    if new_height == last_height:
        break

    last_height = new_height

# FIM DO SCROLLING ATÉ O FINAL DA PÁGINA - PADRÃO


# /html/body/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/main/article[1]/a/div --> FULL XPATH PEGOU TODA A DIV COM NOME E PREÇO

product_elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/main/article[1]/a/div')

for product in product_elements:
    product_text = product.text
    product_lines = product_text.split('\n')

    product_name = product_lines[1]  # Nome do produto
    preco_de = product_lines[2].split(' ')[1]  # Preço original
    preco_por = product_lines[3].split(' ')[1]  # Preço com desconto

    print(f"Nome do produto: {product_name}")
    print(f"De: R$ {preco_de}")
    print(f"Por: R$ {preco_por}")


# Fechando o driver
driver.quit()




#____ ____ ____ ____    ____ ____ ___  _ ____ ____       ____    ___  ____ _ _  _ ____ _ ____ ____    ____ ___ ____ ___  ____    ___  ____ ____ ____    ___  _  _ ____ ____ ____ ____    ____ _  _ ____ _    ____ _  _ ____ ____    _ _  _ ____ ____      ___ ____ _  _ ___ ____    ____ ____    _  _ ___  ____ ___ _  _    ____ ____ _  _    ____ ____ ____ ____    ____ ____ ___  _ ____ ____    ___  ____ ____ ____      ___  ___  ____    ____ ____ ____ ____ ____ ____ ____ _  _ ___ ____    ____    _ _ _ _  _ _ _    ____    ___  ____ ____ ____    ___  ____ ____ ____ ____    _  _ ____ ____ _ ____ ____
#|___ [__  [__  |___    |    |  | |  \ | | __ |  |       |__|    |__] |__/ | |\/| |___ | |__/ |__|    |___  |  |__| |__] |__|    |__] |__| |__/ |__|    |__] |  | [__  |    |__| |__/    |  | |  | |__| |    |  | |  | |___ |__/    | |\ | |___ |  |       |  |___  \/   |  |___    |  | [__      \/  |__] |__|  |  |__|    |    |  | |\/|    |___ [__  [__  |___    |    |  | |  \ | | __ |  |    |__] |__| [__  |___      |  \ |__] [__     |__| |    |__/ |___ [__  |    |___ |\ |  |  |___    |  |    | | | |__| | |    |___    |__] |__| |__/ |__|    |__] |___ | __ |__| |__/    |  | |__| |__/ | |  | [__
#|___ ___] ___] |___    |___ |__| |__/ | |__] |__|       |  |    |    |  \ | |  | |___ | |  \ |  |    |___  |  |  | |    |  |    |    |  | |  \ |  |    |__] |__| ___] |___ |  | |  \    |_\| |__| |  | |___ |_\| |__| |___ |  \    | | \| |    |__| .     |  |___ _/\_  |  |___    |__| ___]    _/\_ |    |  |  |  |  |    |___ |__| |  |    |___ ___] ___] |___    |___ |__| |__/ | |__] |__|    |__] |  | ___] |___ .    |__/ |    ___]    |  | |___ |  \ |___ ___] |___ |___ | \|  |  |___    |__|    |_|_| |  | | |___ |___    |    |  | |  \ |  |    |    |___ |__] |  | |  \     \/  |  | |  \ | |__| ___]
