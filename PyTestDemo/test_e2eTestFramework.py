from selenium.webdriver import chrome
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
#--chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



def test_e2e():
    #service_obj = Service()
    webdriver.ChromiumDriver
    webdriver.
    driver = webdriver.Chrome()
    driver = webdriver. Chrome(service=service_obj)
    driver.implicitly_wait(4)
    driver.get("http://www.rahulshettyacademy.com/angularpractice/")

    driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click


