import time

import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r"d:\chromedriver.exe")

# 设置隐式等待的超时时间
# 1， 如果在 30 s 之内找到了元素，那么什么时候找到元素，就什么时候运行下面的代码
# 超过 30s 没有找到，只能报错。不交 NoSuchElement,  TimeOutException.

driver.implicitly_wait(30)

driver.get("file:///D:/%E7%8F%AD%E7%BA%A7%E7%AE%A1%E7%90%86/python26%E6%9C%9F/web_05_%E7%AD%89%E5%BE%85%E5%92%8C%E5%88%87%E6%8D%A2/iframe_demo.html")

# iframe的切换
# 1, 索引， 从 0 开始
# # 2， name 属性
# # 3,  WebElement 对象
# # 4, locator ('xpath', '...')

# driver.switch_to.frame('baidu')
# 等待
# wait = WebDriverWait(driver, 20)
# wait.until(EC.frame_to_be_available_and_switch_to_it( 'baidu' ))

e = driver.find_element_by_name('mfile')
e.click()

# pyperclip.copy('D:\用户.html')
#
# time.sleep(2)
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.press('enter', presses=2)


from pywinauto import application



# driver.find_element_by_id('upload_pic').click()   # 点击上传/浏览按钮
time.sleep(2)                      # 需要稍作等待，因为点击上传按钮到文件选择窗口打开会有延迟
app = application.Application()   # 实例化Application
# 这里用的class而没有加窗口title，主要为了保证兼容性
app.connect(class_name='#32770')    #根据class_name找到弹出窗口
app["Dialog"]["Edit1"].type_keys("D:\用户.html")     # 在输入框中输入值
app["Dialog"]["Button1"].click()
