from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver): #class constructure
        self.driver = driver
        self.username_input = (By.ID, "username") #this is tuple
        self.password = (By.NAME, "password")
        self.sign_button = (By.ID, "signInBtn")




    def login(self):
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy") #we are using '*' to divide the tuple in two parts.
        self.driver.find_element(*self.password).send_keys("learning")
        self.driver.find_element(*self.sign_button).click()
