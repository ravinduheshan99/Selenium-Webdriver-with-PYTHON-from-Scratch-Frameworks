from selenium.webdriver.common.by import By
from PytestPythonSeleniumFramework.pageObjects.shopPage import ShopPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.signInBtn = (By.ID, "signInBtn")


    def login(self,username,password):
        #By using a * the tuple will be breakdown into two arguments which is expecting by find_element method
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signInBtn).click()
        shopPage = ShopPage(self.driver)
        return shopPage