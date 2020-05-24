import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
# driver.maximize_window()
driver.get("http://www.baidu.com")

setting = driver.find_element(By.XPATH, "//div[@id='u1']//a[@name='tj_settingicon']")
# 鼠标移动到设置位置
action = ActionChains(driver)
action.move_to_element(setting).perform()

elem_gaojishezhi=driver.find_element(By.XPATH,"//div[@class='bdpfmenu']//a[text()='高级搜索']")
action.click(elem_gaojishezhi)
action.perform()



# #select操作
# elem_xiala=driver.find_element(By.NAME,'ft')
# elem_xiala.click()

elem_xiala=driver.find_element(By.NAME,'ft')
select=Select(elem_xiala)
select.select_by_value("xls")

time.sleep(5)
driver.quit()
