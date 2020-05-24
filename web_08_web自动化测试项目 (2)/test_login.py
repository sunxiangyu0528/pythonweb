"""测试登录功能。

流程：
1，启动浏览器，打开url;
2, 定位用户名；
3， 输入用户名；
4， 定位密码；
5， 输入密码；
6， 定位登录按钮；
7， 点击登录按钮；
8，定位错误信息断言
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# 启动浏览器配置 chromedriver 的路径
# driver_path = r'‪C:\chromedriver_71.exe'
driver = webdriver.Chrome()

# 设置隐式等待
wait_timeout = 20
driver.implicitly_wait(wait_timeout)

# 打开 url
host = 'http://120.78.128.25:8765'
# login url
login_api = '/Index/login.html'
login_url = host + login_api
driver.get(login_url)

# 定位用户名；
# driver.find_element_by_id()
# 用户名元素定位方式
mobile_locator = (By.NAME, 'phone')
user_elem = driver.find_element(*mobile_locator)

# 3， 输入用户名；
username = ''
user_elem.send_keys(username)

# 4， 定位密码；
pwd_locator = (By.NAME, 'password')
pwd_elem = driver.find_element(*pwd_locator)

# 5, 输入密码
pwd = ''
pwd_elem.send_keys(pwd)

# 6, 定位登录按钮；
btn_locator = (By.XPATH, "//button[@class='btn btn-special']")
btn_elem = driver.find_element(*btn_locator)

# 7,点击登录按钮；
btn_elem.click()

# 定位错误信息断言
error_info_locator = (By.XPATH, "//div[@class='form-error-info']")
error_elem = driver.find_element(*error_info_locator)
print(error_elem.text)

expected = '请输入手机号吗'
assert error_elem.text == expected

driver.quit()
