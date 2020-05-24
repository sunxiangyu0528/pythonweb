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

# driver.execute_script('document.title')

time.sleep(1)
js_code = 'arguments[0].readOnly = false;'  # ===> e.readOnly = false;
driver.execute_script(js_code, input_elem)

time.sleep(1)
time_str = "2020-05-03"
js_code = "arguments[0].value = '{}';".format(time_str)
driver.execute_script(js_code, input_elem)

time.sleep(3)
driver.quit()

