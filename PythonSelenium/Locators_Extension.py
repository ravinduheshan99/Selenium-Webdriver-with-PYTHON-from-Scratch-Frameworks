import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

current_dir = os.path.dirname(__file__)
dirver_path = os.path.join(current_dir,"..","resources","chromedriver-win64","chromedriver.exe")
driver_path = os.path.abspath(dirver_path)
service_obj = Service(driver_path)
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client")

driver.find_element(By.LINK_TEXT,"Forgot password?").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"password").click()

driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("test@gmail.com")
driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("test@123")
driver.find_element(By.XPATH,"form div:nth-child(3) input").send_keys("test@123")

driver.find_element(By.XPATH,"//button[@type='submit']").click()
# driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()