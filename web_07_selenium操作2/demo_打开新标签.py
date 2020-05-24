import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r"d:\chromedriver.exe")

# 添加隐士等待
driver.implicitly_wait(30)

driver.get("https://www.12306.cn/index/")

# 打开，新窗口
def new_tab(driver):
    """打开新窗口"""
    driver.execute_script("window.open();")
    # pull request

# driver.execute_script("window.open();")



