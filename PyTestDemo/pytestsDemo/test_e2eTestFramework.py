from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.login import LoginPage


def test_e2e(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    # Login
    loginPage = LoginPage(driver)
    loginPage.login()

    driver.maximize_window()

    # Navigate to shop
    driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    for product in products:
        productName = product.find_element(By.XPATH, "div/h4/a").text
        if productName == "Blackberry":
            product.find_element(By.XPATH, "div/button").click()
            break  # stop after adding the product

    # Checkout
    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'btn-primary')]"))
    )
    button.click()

    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    # Country selection
    driver.find_element(By.ID, "country").send_keys("ind")
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()

    # Terms and submit
    driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Assertion
    successText = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Success! Thank you!" in successText