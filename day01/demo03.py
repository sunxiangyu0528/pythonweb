from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("")

driver.switch_to.frame()
