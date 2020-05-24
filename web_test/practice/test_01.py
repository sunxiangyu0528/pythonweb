from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

elem=driver.find_element(By.ID,"kw")
elem.send_keys("柠檬班",Keys.ENTER)
# elem.send_keys(Keys.ENTER)

driver.quit()