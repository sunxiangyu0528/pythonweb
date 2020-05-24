import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r"d:\chromedriver.exe")

# 添加隐士等待
driver.implicitly_wait(30)

driver.get("http://www.baidu.com")

input_elem = driver.find_element_by_id('kw')

input_elem.send_keys('柠檬班')

# 输入回车，在元素上调用， send_keys()
input_elem.send_keys(Keys.ENTER)

time.sleep(2)

driver.quit()

By
# locator = ('id', 'kw')
# driver.find_element(*locator)
