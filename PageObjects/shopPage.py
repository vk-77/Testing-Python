from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.checkout_confirmation import Checkout_Confirmation
from utils.browserUtils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.XPATH, "//a[contains(@class,'btn-primary')]")

    def add_product_to_cart(self, product_name):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_cards)

        for product in products:
            product_name_text = product.find_element(By.XPATH, "div/h4/a").text
            if product_name_text == product_name:
                product.find_element(By.XPATH, "div/button").click()
                break

    def goToCart(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.checkout_button)).click()
        return Checkout_Confirmation(self.driver)