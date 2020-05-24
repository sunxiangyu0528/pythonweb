import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r"d:\chromedriver.exe")

# 设置隐式等待的超时时间
# 1， 如果在 30 s 之内找到了元素，那么什么时候找到元素，就什么时候运行下面的代码
# 超过 30s 没有找到，只能报错。不交 NoSuchElement,  TimeOutException.

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://www.baidu.com")

# 找到设置选项
setting = driver.find_element_by_xpath("//div[@id='u1']//a[@name='tj_settingicon']")

# 鼠标移动到设置按钮
action = ActionChains(driver)
action.move_to_element(setting)
action.perform()

gaoji_setting = driver.find_element_by_xpath("//div[@class='bdpfmenu']//a[text()='高级搜索']")
action.click(gaoji_setting)
action.perform()

# action_chains.click(on_element)
# element.click()


# 正确：ActionChains(driver).move_to_element(setting).perform()

# ac = ActionChains(driver)
# ac.move_to_element(setting).click(..).drag_and_drop(...).context_click(...).click(..)
# ac.perform()


# select 操作 方法1：直接定位 option 元素，点击
# 定位 option
# option = driver.find_element_by_xpath("//option[@value='xls']")
# time.sleep(2)
# option.click()

# 方法2： 更加复杂，但是可读性，可靠性强， 用到 selenium， Select
s_elem = driver.find_element_by_xpath("//select[@name='ft']")
s_elem.send_keys(Keys.ENTER)
select = Select(s_elem)
# 选择
select.select_by_value('xls')
select.select_by_index()
select.select_by_visible_text()



time.sleep(3)
# 退出
driver.quit()

Keys