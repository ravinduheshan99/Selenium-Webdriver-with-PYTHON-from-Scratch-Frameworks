import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

current_dir = os.path.dirname(__file__)
dirver_path = os.path.join(current_dir,"..","resources","chromedriver-win64","chromedriver.exe")
driver_path = os.path.abspath(dirver_path)
service_obj = Service(driver_path)
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action = ActionChains(driver)
#action.double_click()
#action.context_click()
#action.context_click()
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click()