import time

from selenium import webdriver #importing the webdriver to launch a browser.
from selenium.webdriver.common.by import By

#chrome driver service.
driver = webdriver.Chrome()

driver.get("https://login.allypro.tech/") #Getting the URL on the charome browser.
driver.maximize_window()
print("Screen title is: ",driver.title)
print("Page URL is : ",driver.current_url)

driver.find_element(By.ID,"CompanyName").send_keys("allypro")
driver.find_element(By.ID,"Email").send_keys("vishal.kumar@routeware.com")
driver.find_element(By.ID,"EncryptedPassword").send_keys("@llyPro$")

driver.find_element(By.CLASS_NAME,"custom_login_btn").click()






time.sleep(3)