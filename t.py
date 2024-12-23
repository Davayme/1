import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select


driver = webdriver.Edge()
driver.get("http://127.0.0.1:5500/index.html")
time.sleep(2)

btnAddProduct = driver.find_element(By.ID, "btnAddProduct")
btnAddProduct.click()

inputCode = driver.find_element(By.ID, "product-code")
inputName = driver.find_element(By.ID, "product-name")
inputPrice = driver.find_element(By.ID, "product-price")
inputCost = driver.find_element(By.ID, "product-cost")
inputStock = driver.find_element(By.ID, "product-stock")
inputType = driver.find_element(By.ID, "product-type")
inputImage = driver.find_element(By.ID, "product-image")
inputDate= driver.find_element(By.ID, "product-date")

inputCode.send_keys("1")
time.sleep(1)
inputName.send_keys("Doritos")
time.sleep(1)
inputPrice.send_keys("20")
time.sleep(1)
inputCost.send_keys("2")
time.sleep(1)
inputStock.send_keys("20")
time.sleep(1)
Select(inputType).select_by_value("Food")
time.sleep(1)
inputImage.send_keys("C:/Users/davay/Downloads/1/1/logo.png", )
time.sleep(1)
inputDate.send_keys("23-12-2024")
time.sleep(1)

btnSave = driver.find_element(By.ID, "btn-save")
btnSave.click()
time.sleep(2)


btnAddProduct.click()
time.sleep(2)
inputCode.send_keys("2")
time.sleep(1)
inputName.send_keys("Doritos")
time.sleep(1)
inputPrice.send_keys("20")
time.sleep(1)
inputCost.send_keys("2")
time.sleep(1)
inputStock.send_keys("20")
time.sleep(1)
Select(inputType).select_by_value("Food")
time.sleep(1)
inputImage.send_keys("C:/Users/davay/Downloads/1/1/logo.png")
time.sleep(1)
inputDate.send_keys("23-12-2024")
time.sleep(1)

btnSave.click()
time.sleep(2)

btEdit = driver.find_elements(By.CLASS_NAME, "edit-btn")
btEdit[1].click()
time.sleep(1)

alert = Alert(driver)

alert.accept()
time.sleep(1)
alert.accept()
time.sleep(1)
alert.accept()
time.sleep(1)

alert.accept()
time.sleep(1)

alert.accept()
time.sleep(1)

alert.send_keys("Electronics")
alert.accept()
time.sleep(1)

btnDelete = driver.find_elements(By.CLASS_NAME, "delete-btn")
btnDelete[0].click()
alert.accept()
time.sleep(5)
