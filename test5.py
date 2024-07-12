from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import openpyxl

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# site alvo
url = 'https://www.magazineluiza.com.br/celulares-e-smartphones/l/te/'

# obter o conteudo do mesmo
driver.get(url)

# instanciando a minha lista de itens
items = []

# Instanciar altura da página
last_height = driver.execute_script('return document.body.scrollHeight')

# Definir contagem
itemTargetCount = 25

# Escrolar pagina até o fim
while itemTargetCount > len(items):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    # Wait for content to load
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')

    if new_height == last_height:
        break

    last_height = new_height

    # Select elements by XPath
    product_elements = driver.find_elements(By.XPATH, '//div[@data-testid="product-card-content"]')
    for product in product_elements:
        try:
            name_element = product.find_element(By.XPATH, './/h2[@data-testid="product-title"]')
            name = name_element.text.strip()

            price_original_element = product.find_element(By.XPATH, './/p[@data-testid="price-original"]')
            price_original = price_original_element.text.strip()

            price_value_element = product.find_element(By.XPATH, './/p[@data-testid="price-value"]')
            price_value = price_value_element.text.strip()

            items.append({"name": name, "price_original": price_original, "price_value": price_value})
        except NoSuchElementException:
            print("Elemento não encontrado. Pulando para o próximo.")

# Close the driver
driver.quit()

# Saving to Excel file
excel_file = "magazineluiza_products.xlsx"

# Create a workbook and select the active sheet
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Magazine Luiza Products"

# Write headers
sheet["A1"] = "Name"
sheet["B1"] = "Price Original"
sheet["C1"] = "Price Value"

# Write data
row = 2
for item in items:
    sheet[f"A{row}"] = item["name"]
    sheet[f"B{row}"] = item["price_original"]
    sheet[f"C{row}"] = item["price_value"]
    row += 1

# Save workbook
workbook.save(filename=excel_file)
print(f"Dados salvos em '{excel_file}'")
