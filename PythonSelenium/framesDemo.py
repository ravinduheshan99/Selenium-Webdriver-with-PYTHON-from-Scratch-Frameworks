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

driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")

driver.switch_to.default_content()
visibleText = driver.find_element(By.CSS_SELECTOR,"h3").text
assert visibleText == "I am able to automate frames"