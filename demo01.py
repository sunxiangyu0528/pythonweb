from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://www.baidu.com")
print(driver.title)
driver.quit()