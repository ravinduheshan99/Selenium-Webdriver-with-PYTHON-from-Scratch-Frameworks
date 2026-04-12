import os
from selenium import webdriver
from selenium.webdriver.ie.service import Service

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("headless")
chromeOptions.add_argument("--ignore-certificate-errors")

current_dir = os.path.dirname(__file__)
dirver_path = os.path.join(current_dir,"..","resources","chromedriver-win64","chromedriver.exe")
driver_path = os.path.abspath(dirver_path)
service_obj = Service(driver_path)
driver = webdriver.Chrome(service=service_obj, options=chromeOptions)

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("jsExecutorMiscellanous.png")