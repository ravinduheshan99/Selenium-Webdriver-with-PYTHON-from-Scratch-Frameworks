from selenium.webdriver.common.by import By
from PytestPythonSeleniumFramework.pageObjects.checkoutConfirmationPage import CheckOutConfirmationPage
from PytestPythonSeleniumFramework.utils.browser_utils import BrowserUtils


class ShopPage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.goto_checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def add_product_to_cart(self,product_name):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_cards)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                product.find_element(By.XPATH, "div/button").click()


    def goToCart(self):
        self.driver.find_element(*self.goto_checkout_button).click()
        checkoutConfirmationPage = CheckOutConfirmationPage(self.driver)
        return checkoutConfirmationPage
