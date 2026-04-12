import os
import time

from selenium import webdriver
from selenium.webdriver.ie.service import Service

"""

# Get current file directory
current_dir = os.path.dirname(__file__)

# Navigate to project root -> resources -> chromedriver
driver_path = os.path.join(current_dir,"..","resources","chromedriver-win64","chromedriver.exe")

# Normalize path (important for Windows)
driver_path = os.path.abspath(driver_path)

service_obj = Service(driver_path)
driver = webdriver.Chrome(service=service_obj)

"""

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print("Current Page URL: ",driver.current_url)
print("Current Page Title: ",driver.title)
time.sleep(2)
