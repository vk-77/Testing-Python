from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(3)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
#driver.find_element(By.ID,'tinymce').clear()
#driver.find_element(By.ID,"tinymce").send_keys("I am able to Automate frames")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
