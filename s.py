import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select

# Inicializa el controlador de Edge
driver = webdriver.Edge()

# Abre la página web
driver.get("http://127.0.0.1:5500/index.html")
time.sleep(2)

# Encuentra y hace clic en el botón para agregar un producto
btnAddProduct = driver.find_element(By.ID, "btnAddProduct")
btnAddProduct.click()
time.sleep(1)

# Encuentra los campos de entrada del formulario
inputProduct = driver.find_element(By.ID, "product-code")
inputName = driver.find_element(By.ID, "product-name")
inputPrice = driver.find_element(By.ID, "product-price")
inputCost = driver.find_element(By.ID, "product-cost")
inputStock = driver.find_element(By.ID, "product-stock")
inputSelectType = driver.find_element(By.ID, "product-type")

# Rellena el formulario con datos del primer producto
inputProduct.send_keys("001")
time.sleep(1)
inputName.send_keys("Producto 1")
time.sleep(1)
inputPrice.send_keys("100")
time.sleep(1)
inputCost.send_keys("50")
time.sleep(1)
inputStock.send_keys("10")
time.sleep(1)
Select(inputSelectType).select_by_value("Food")
time.sleep(1)

# Guarda el primer producto
btnSave = driver.find_element(By.ID, "btn-save")
btnSave.click()
time.sleep(2)

# Repite el proceso para un segundo producto
btnAddProduct.click()
inputProduct.send_keys("002")
time.sleep(1)
inputName.send_keys("Producto 2")
time.sleep(1)
inputPrice.send_keys("100")
time.sleep(1)
inputCost.send_keys("50")
time.sleep(1)
inputStock.send_keys("10")
time.sleep(1)
Select(inputSelectType).select_by_value("Clothing")
time.sleep(1)
btnSave = driver.find_element(By.ID, "btn-save")
btnSave.click()
time.sleep(2)

# Encuentra y hace clic en el botón de editar del segundo producto
editbtn = driver.find_elements(By.CLASS_NAME, "edit-btn")
editbtn[1].click()

# Maneja la alerta para editar el producto
alert = Alert(driver)
alert.send_keys("003")
alert.accept()
time.sleep(1)

alert.send_keys("Producto 3")
alert.accept()
time.sleep(1)
alert.send_keys("3")
alert.accept()
time.sleep(1)
alert.send_keys("3")
alert.accept()
time.sleep(1)
alert.send_keys("3")
alert.accept()
time.sleep(1)
alert.send_keys("Food")
alert.accept()
time.sleep(1)

# Encuentra y hace clic en el botón de eliminar del segundo producto
eliminarbtn = driver.find_elements(By.CLASS_NAME, "delete-btn")
eliminarbtn[1].click()
time.sleep(1)
alert.accept()
time.sleep(2)

# Cierra el navegador
driver.quit()