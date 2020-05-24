from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

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


elem_Sel=driver.find_element(By.XPATH,"//select[@name='ft']")


select=Select(elem_Sel)
select.select_by_value("doc")