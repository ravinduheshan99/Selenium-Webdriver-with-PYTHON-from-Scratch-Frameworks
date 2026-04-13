import os
import pytest
from selenium import webdriver
from selenium.webdriver.ie.service import Service
# command to pass execution browser ---> pytest test_e2eTestFramework.py --browser_name firefox

driver = None

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help='browser selection')


@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
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
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "edge":
        driver = webdriver.Edge(service=service_obj)

    driver.implicitly_wait(8)
    driver.get("https://rahulshettyacademy.com/loginpagePractise")
    #Executing before test function execution
    yield driver
    #Executiong post your test function execution
    driver.close()


@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), "reports")
            os.makedirs(reports_dir, exist_ok=True)

            file_name = report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_") + ".png"
            file_path = os.path.join(reports_dir, file_name)

            print("file path is " + file_path)
            _capture_screenshot(file_path)

            if file_name:
                html = (
                    f'<div><img src="{file_name}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)