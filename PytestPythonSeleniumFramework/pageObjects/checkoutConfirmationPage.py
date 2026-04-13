from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PytestPythonSeleniumFramework.utils.browser_utils import BrowserUtils


class CheckOutConfirmationPage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.CSS_SELECTOR, "input[type='submit']")
        self.success_message = (By.CLASS_NAME, "alert-success")
        self.wait = WebDriverWait(self.driver, 10)


    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()


    def enter_delivery_address(self,partialCountryName,fullCountryName):
        self.driver.find_element(*self.country_input).send_keys(partialCountryName)
        self.wait.until(EC.presence_of_element_located(self.country_option))
        self.driver.find_element(By.LINK_TEXT, fullCountryName).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()


    def validate_order(self):
        self.wait.until(EC.presence_of_element_located(self.success_message))
        successText = self.driver.find_element(*self.success_message).text
        return successText