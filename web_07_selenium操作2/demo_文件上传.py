import time

import pyperclip
from pywinauto import application
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r"d:\chromedriver.exe")

# 添加隐士 GH等待
driver.implicitly_wait(30)

driver.get("file:///D:/%E7%8F%AD%E7%BA%A7%E7%AE%A1%E7%90%86/python26%E6%9C%9F/web_05_%E7%AD%89%E5%BE%85%E5%92%8C%E5%88%87%E6%8D%A2/iframe_demo.html")

# 元素定位
e = driver.find_element_by_name("mfile")
e.click()
# e.send_keys(r"D:\home.html")
#
# time.sleep(2)
# driver.quit()

# time.sleep(2)                      # 需要稍作等待，因为点击上传按钮到文件选择窗口打开会有延迟
# app = application.Application()   # 实例化Application
# # 这里用的class而没有加窗口title，主要为了保证兼容性
# app.connect(class_name='#32770')    #根据class_name找到弹出窗口
# app["Dialog"]["Edit1"].type_keys("D:\用户.html")     # 在输入框中输入值
# app["Dialog"]["Button1"].click()

# pyautogui (跨平台)

import pyautogui as ui
# 发送数据
pyperclip.copy('D:\用户.html')
time.sleep(2)
ui.hotkey('ctrl', 'v')

time.sleep(2)
ui.press('enter', presses=2)

time.sleep(4)
