import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.rahulshettyacademy.com/angularpractice/")

"""driver.maximize_window()
pageTitle = driver.title
print("Title is = ", pageTitle)
PageURL = driver.current_url
print("Page URL is = ",PageURL)"""

driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()

#to write the Xpath : //tagname[@attribute='Value'] -> //input[@type='submit']

driver.find_element(By.CSS_SELECTOR,"input[name = 'name']").send_keys("Mr QA")
driver.find_element(By.ID,'inlineRadio1').click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello Again")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()







time.sleep(3)

