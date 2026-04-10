import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#Click on column header
#Collect the browserSortedVeggieList
#Create a manually sorted list as manualSortedList
#browserSortedVeggieList == manualSortedList

current_dir = os.path.dirname(__file__)
dirver_path = os.path.join(current_dir,"..","resources","chromedriver-win64","chromedriver.exe")
driver_path = os.path.abspath(dirver_path)
service_obj = Service(driver_path)
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
veggieWebElemenets = driver.find_elements(By.XPATH,"//tr/td[1]")

browserSortedVeggieList = []

for element in veggieWebElemenets:
    browserSortedVeggieList.append(element.text)

originalBrowserSortedList = browserSortedVeggieList.copy()
#originalBrowserSortedList = browserSortedVeggieList.slice()

browserSortedVeggieList.sort()
assert browserSortedVeggieList == originalBrowserSortedList