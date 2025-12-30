from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)

#ran the script but it didn't run in headless mode.
