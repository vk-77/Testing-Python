from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import service
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("headless")

driver = webdriver.Firefox()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

driver.get_screenshot_as_file("screen.png")