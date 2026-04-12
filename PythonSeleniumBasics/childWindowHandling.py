import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

current_dir = os.path.dirname(__file__)
dirver_path = os.path.join(current_dir,"..","resources","chromedriver-win64","chromedriver.exe")
driver_path = os.path.abspath(dirver_path)
service_obj = Service(driver_path)
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Click Here").click()

allWindowHandles = driver.window_handles

driver.switch_to.window(allWindowHandles[1])
textInChildWindow = driver.find_element(By.TAG_NAME,"h3").text
assert textInChildWindow == "New Window"
driver.close()

driver.switch_to.window(allWindowHandles[0])
textParentWindow = driver.find_element(By.TAG_NAME,"h3").text
assert textParentWindow == "Opening a new window"

