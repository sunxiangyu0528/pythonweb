import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://120.78.128.25:8765/Index/login.html")


elem_phone=driver.find_element(By.NAME,"phone")
elem_phone.send_keys("")
elem_pwd=driver.find_element(By.NAME,"password")
elem_pwd.send_keys("13")
elem_denglu=driver.find_element(By.XPATH,"//div/button[text()='登录']").click()
# print(elem_denglu.text)

elem_error=driver.find_element(By.XPATH,"//div[text()='请输入手机号']")
print(elem_error.text)
time.sleep(4)
driver.quit()