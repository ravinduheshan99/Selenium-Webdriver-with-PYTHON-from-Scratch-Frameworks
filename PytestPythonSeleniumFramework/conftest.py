import pytest
import os
from selenium import webdriver
from selenium.webdriver.ie.service import Service

# command to pass execution browser ---> pytest test_e2eTestFramework.py --browser_name firefox


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help='browser selection')


@pytest.fixture(scope="function")
def browserInstance(request):
    """
    current_dir = os.path.dirname(__file__)
    dirver_path = os.path.join(current_dir, "..", "resources", "chromedriver-win64", "chromedriver.exe")
    driver_path = os.path.abspath(dirver_path)
    service_obj = Service(driver_path)
    driver = webdriver.Chrome(service=service_obj)
    """
    browser_name = request.config.getoption("browser_name")
    service_obj = Service()
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service_obj)
        driver.implicitly_wait(5)

    #Executing before test function execution
    yield driver
    #Executiong post your test function execution
    driver.close()