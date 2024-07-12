from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import openpyxl

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)

# Load target website
url = 'https://www.dafiti.com.br/roupas-masculinas/camisas/'

# Get website content
driver.get(url)

# Instantiate items
items = []

# Instantiate height of webpage
last_height = driver.execute_script('return document.body.scrollHeight')

# Set target count
itemTargetCount = 20

# Scroll to bottom of webpage
while itemTargetCount > len(items):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    # Wait for content to load
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')

    if new_height == last_height:
        break

    last_height = new_height

    # Select elements by XPath
    product_elements = driver.find_elements(By.CLASS_NAME, "product-box-detail")
    for product in product_elements:
        try:
            name = product.find_element(By.CLASS_NAME, "product-box-title").text
            price_from = product.find_element(By.CLASS_NAME, "product-box-price-from").text
            price_to_element = product.find_element(By.CLASS_NAME, "product-box-price-to")
            price_to = price_to_element.text if price_to_element else "Preço não disponível"
            items.append({"name": name, "price_from": price_from, "price_to": price_to})
        except NoSuchElementException:
            print("Elemento não encontrado. Pulando para o próximo.")

# Close the driver
driver.quit()

# Saving to Excel file
excel_file = "dafiti_products.xlsx"

# Create a workbook and select the active sheet
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Dafiti Products"

# Write headers
sheet["A1"] = "Name"
sheet["B1"] = "Price From"
sheet["C1"] = "Price To"

# Write data
row = 2
for item in items:
    sheet[f"A{row}"] = item["name"]
    sheet[f"B{row}"] = item["price_from"]
    sheet[f"C{row}"] = item["price_to"]
    row += 1

# Save workbook
workbook.save(filename=excel_file)
print(f"Dados salvos em '{excel_file}'")
