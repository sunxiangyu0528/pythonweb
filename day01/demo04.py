import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://www.baidu.com")

setting=driver.find_element_by_xpath("//a[@id='s_usersetting_top']//span[@class='setting-text']")

action=ActionChains(driver)
action.move_to_element(setting).perform()

time.sleep(5)

driver.quit()
