import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.select import Select

current_dir = os.path.dirname(__file__)
dirver_path = os.path.join(current_dir,"..","resources","chromedriver-win64","chromedriver.exe")
driver_path = os.path.abspath(dirver_path)
service_obj = Service(driver_path)
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# To create CSSSelector -> tagname[attribute='value of the attribute'], #ID, .Classname
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Ravindu Haputhanthri")

# ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME,"email").send_keys("contact@rahulshetty.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Rs@12345")
driver.find_element(By.ID,"exampleCheck1").click()

# Static Dropdown
staticDropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
staticDropdown.select_by_index(1)
staticDropdown.select_by_visible_text("Male")

# Select Radio Button
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1")

# To create Xpath -> //tagname[@attribute='value of the attribute']
driver.find_element(By.XPATH,"//input[@type='submit']").click()
successMessage = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success" in successMessage
print("Assertion successed with final success message: ",successMessage)

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello Again!")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()



