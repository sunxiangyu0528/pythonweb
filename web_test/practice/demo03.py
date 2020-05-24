import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# 添加隐士等待
driver.implicitly_wait(30)

driver.get("https://www.12306.cn/index/")

# 元素定位
input_elem = driver.find_element_by_id('train_date')

js_code="document.getElementById(train_date)"

s=driver.execute_script(js_code)
print(s)