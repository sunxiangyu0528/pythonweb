from selenium import webdriver

# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver=webdriver.Chrome()

driver.get("http://www.baidu.com")

driver.find_element_by_xpath(r'//input[@id="kw"]').send_keys("柠檬班")
#获取当前窗口
windows=driver.window_handles
#打开柠檬班
driver.find_element_by_id("su").click()
#等待窗口被打开
wait=WebDriverWait(driver,30)
wait.until(ec.new_window_is_opened(windows))

#进行窗口切换
window=driver.window_handles[-1]

driver.switch_to.window(window)



#定位华华老师
driver.find_element_by_xpath('//h4[text()="华华老师"]').click()







#初始化一个计时器
# wait=WebDriverWait(driver,timeout=30,poll_frequency=0.1)
# #条件
# loader=("xpath",'//*[contains(text(),"_腾讯课堂")]')

# element=wait.until(ec.presence_of_element_located(loader))  #某一个元素被加载出来
# wait.until(ec.visibility_of_all_elements_located(loader))   #等待元素可见
# wait.until(ec.element_to_be_clickable())  #等待元素可以被点击


