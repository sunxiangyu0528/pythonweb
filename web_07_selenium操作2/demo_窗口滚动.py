import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r"d:\chromedriver.exe")

# 添加隐士等待
driver.implicitly_wait(30)

driver.get("https://www.12306.cn/index/")

e = driver.find_element_by_class_name('mr')

# 将元素滑动到可见区域（为了点击或者其他的进一步操作）
# e.location_once_scrolled_into_view
e.location_once_scrolled_into_view

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

time.sleep(2)

