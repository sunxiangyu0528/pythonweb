import time
from selenium import webdriver
# from selenium.webdriver import
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://lemon.ke.qq.com/")
setting=driver.find_element_by_xpath('//a[text()="分类"]')

action=ActionChains(driver)
action.move_to_element(setting).perform()



time.sleep(3)
driver.quit()