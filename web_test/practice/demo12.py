import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.12306.cn/index/")

# elem=driver.find_element(By.XPATH,"//*[@data-click='train_date']")
elem=driver.find_element_by_id('train_date')
# js_code="e=document.getElementById('train_date');"


# e=driver.execute_script(js_code)


js_code="arguments[0].readonly=false;"
driver.execute_script(js_code,elem)
time.sleep(1)

js_code2="arguments[0].value='2020-05-03';"


driver.execute_script(js_code2,elem)

