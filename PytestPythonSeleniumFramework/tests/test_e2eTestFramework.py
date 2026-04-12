import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import json
import pytest
from PytestPythonSeleniumFramework.pageObjects.loginPage import LoginPage
from pathlib import Path


test_data_path = Path(__file__).parent.parent / "data" / "e2eFrameworkData.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    driver.maximize_window()

    loginPage = LoginPage(driver)
    shopPage = loginPage.login(test_list_item["userName"],test_list_item["userPassword"])

    shopPage.add_product_to_cart(test_list_item["productName"])
    checkoutConfirmationPage = shopPage.goToCart()

    checkoutConfirmationPage.checkout()
    checkoutConfirmationPage.enter_delivery_address(test_list_item["partialCountryName"],test_list_item["fullCountryName"])
    successText = checkoutConfirmationPage.validate_order()
    assert test_list_item["actualTextToAssert"] in successText

