from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

url = 'https://www.kabum.com.br/computadores/notebooks/notebook-acer'
driver.get(url)

try:
    # Aumenta o tempo de espera inicial para carregar a página completamente
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="sc-fzoMdx eUNqBj productCard"]')))

    # Definindo a quantidade alvo de informações a ser coletadas
    itemTargetCount = 20

    # Lista para armazenar os produtos encontrados
    items = []

    # INICIO DO SCROLLING ATÉ O FINAL DA PÁGINA
    while len(items) < itemTargetCount:
        # Scroll até o final da página
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

        # Aguarda um curto período para carregar os novos elementos
        time.sleep(2)

        # Encontra todos os elementos de produto na página
        product_elements = driver.find_elements(By.XPATH, '//div[@class="sc-fzoMdx eUNqBj productCard"]')

        # Itera sobre os elementos de produto encontrados
        for product in product_elements:
            product_text = product.text
            items.append(product_text)

        # Verifica se o número alvo de produtos foi alcançado
        if len(items) >= itemTargetCount:
            break

    # FIM DO SCROLLING ATÉ O FINAL DA PÁGINA - PADRÃO

    # Processa os primeiros 20 produtos encontrados
    for product in items[:itemTargetCount]:
        product_lines = product.split('\n')

        # Verifica se o produto possui todas as informações necessárias
        if len(product_lines) >= 4:
            product_name = product_lines[0]  # Nome do produto
            preco_de = product_lines[1]  # Preço original
            preco_por = product_lines[2]  # Preço com desconto

            print(f"Nome do produto: {product_name}")
            print(f"De: {preco_de}")
            print(f"Por: {preco_por}")
        else:
            print("Produto sem informações suficientes:", product_lines)

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

finally:
    # Fechando o driver apenas se estiver aberto
    if driver:
        driver.quit()
