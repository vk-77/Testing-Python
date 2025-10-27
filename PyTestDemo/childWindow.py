from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.service import service
from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(3)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowOpened = driver.window_handles

driver.switch_to.window(windowOpened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()

driver.switch_to.window(windowOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text