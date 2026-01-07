from selenium.webdriver.common.by import By

from utils.browserUtils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver): #class constructure
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username") #this is tuple
        self.password = (By.NAME, "password")
        self.sign_button = (By.ID, "signInBtn")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username) #we are using '*' to divide the tuple in two parts. "rahulshettyacademy" , "learning"
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
