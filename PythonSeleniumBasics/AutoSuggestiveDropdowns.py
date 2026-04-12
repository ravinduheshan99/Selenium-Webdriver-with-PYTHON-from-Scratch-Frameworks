import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

current_dir = os.path.dirname(__file__)
dirver_path = os.path.join(current_dir,"..","resources","chromedriver-win64","chromedriver.exe")
driver_path = os.path.abspath(dirver_path)
service_obj = Service(driver_path)
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(5)

countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print("Number of countries fetched: ",len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"
print("Final assertion successful with the correct country: ",driver.find_element(By.ID,"autosuggest").get_attribute("value"))




