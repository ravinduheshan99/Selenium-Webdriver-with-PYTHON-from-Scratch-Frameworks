import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--start-maximized')
chromeOptions.add_argument('headless')
chromeOptions.add_argument("--ignore-certificate-errors")

current_dir = os.path.dirname(__file__)
dirver_path = os.path.join(current_dir,"..","resources","chromedriver-win64","chromedriver.exe")
driver_path = os.path.abspath(dirver_path)
service_obj = Service(driver_path)
driver = webdriver.Chrome(service=service_obj, options=chromeOptions)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice")

print(driver.title)