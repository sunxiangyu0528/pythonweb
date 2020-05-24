import time
from selenium import webdriver

#初始化浏览器
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.implicitly_wait(10)
#打开百度

driver.get("http://www.baidu.com")

#定位输出框

elem=driver.find_element(By.ID,"kw")
#输入刘若英
elem.send_keys("柠檬班")

#定位百度一下按钮
elem_baidu=driver.find_element(By.ID,"su")

#点击百度一下
elem_baidu.click()
# time.sleep(1)

#显式等待
#初始化一个计时器
wait=WebDriverWait(driver,timeout=10,poll_frequency=0.1)
#加判断
#某一个元素被加载出来
#presence_of_element_located:等待元素加载
#visibility_of_all_elements_located：等待元素可见
#element_to_be_clickable:元素可被点击
# locater=("xpath",'//a[text()="_腾讯课堂"]')
# wait.until(EC.presence_of_element_located(locater))
#找到柠檬班
elem_lemon=driver.find_element(By.XPATH,'//a[text()="_腾讯课堂"]')

#获取当前窗口
windows=driver.window_handles
#点击
elem_lemon.click()
#此时已经打开框另一个窗口，需要切换窗口
#获取现在的窗口数量
print(driver.window_handles)
#切换窗口
driver.switch_to.window(driver.window_handles[-1])

#新窗口打开需要时间，设置显示等待
wait=WebDriverWait(driver,timeout=10)
wait.until(EC.new_window_is_opened(windows))
#定位华华老师
driver.find_element(By.XPATH,'//h4[text()="华华老师"]')


# time.sleep(4)
#关闭浏览器
driver.quit()