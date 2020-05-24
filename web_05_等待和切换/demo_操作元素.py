"""百度柠檬班"""
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r"d:\chromedriver.exe")

# 设置隐式等待的超时时间
# 1， 如果在 30 s 之内找到了元素，那么什么时候找到元素，就什么时候运行下面的代码
# 超过 30s 没有找到，只能报错。不交 NoSuchElement,  TimeOutException.

driver.implicitly_wait(30)

driver.get("http://www.baidu.com")
input_elem = driver.find_element_by_id('kw')
# 发送用户数据 / 输入用户数据
input_elem.send_keys('柠檬班')

# 定位百度一下， 再点击
# click 是属于一个元素的方法， WebElement
# list
driver.find_element_by_id('su').click()
# baidu_btn = driver.find_element_by_id('su')
# baidu_btn.click()

# 找到柠檬班腾讯课堂, 没有等待，所以找不到元素。
# 只要是出现有动态加载的内容，一定要等待的。
# tx_elem = driver.find_element_by_xpath("//a[contains(text(), 'lemon.ke.qq.com/')]")
# print(tx_elem)

# 等待方式1：强制等待： time.sleep(2)
# 等待方式2：智能等待：
# 隐式等待，显式等待
# TODO: 隐士等待只需要在初始化浏览器之后，设置 1 次 就够了。
# 隐式等待只能用来等待元素被加载（找元素的时候。）
# find_element

# 显式等待
# get, refresh()
# 记住用法
# 初始化一个计时器。
wait = WebDriverWait(driver, 30, poll_frequency=0.1)
# 条件

# presence_of_element_located: 等待元素加载
# visibility_of_element_located: 等待元素可见
# element_to_be_clickable: 等待元素被点击
locator = ('xpath', "//a[contains(text(), 'lemon.ke.qq.com/')]")
element = wait.until(EC.element_to_be_clickable( locator ))
print(element)
# 在点击之前获取所以的窗口
windows = driver.window_handles

# 点击，进入腾讯课堂
element.click()

# 窗口切换
# print(driver.window_handles)
# 切换窗口


# 等待窗口新窗口被打开
wait = WebDriverWait(driver, 20)
# new_window_is_opened(参数：新窗口打开之前的所有的窗口)
wait.until(EC.new_window_is_opened( windows ))

# 有没有完成切换？？？
driver.switch_to.window(driver.window_handles[-1])

# 定位华华老师
huahua = driver.find_element_by_xpath("//h4[text()='华华老师']")
print(huahua)





