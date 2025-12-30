import time

from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# //a[contains(@href,'shop')]  a[href*='shop']

driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()

#time.sleep(5)
#driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()

#//a[@class='nav-link btn btn-primary']
#other way if above is not working.
wait = WebDriverWait(driver, 10)

button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'btn-primary')]"))
)
button.click()

driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME,"alert-success").text

assert "Success! Thank you!" in successText
driver.close()