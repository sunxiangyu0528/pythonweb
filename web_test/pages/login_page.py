from selenium.webdriver.common.by import By

from web_test.config import Setting


class LoginPage:

    login_url = '/Index/login.html'

    btn_locator = (By.XPATH, "//button[@class='btn btn-special']")
    # mobile_locator = (By.NAME, 'phone')

    def __init__(self,driver):
        self.driver=driver

    def get(self):
        host = Setting.host
        # login url
        login_api = Setting.login_url
        login_url = host + self.login_url
        self.driver.get(login_url)

    def login(self,username,pwd):
        """登录操作"""
        # 打开 url
        # host = 'http://120.78.128.25:8765'
        # # login url
        # login_api = '/Index/login.html'
        # login_url = host + login_api
        # self.driver.get(login_url)
        self.get()

        # 定位用户名；
        # driver.find_element_by_id()
        # 用户名元素定位方式
        mobile_locator = (By.NAME, 'phone')
        user_elem = self.driver.find_element(*mobile_locator)

        # 3， 输入用户名；
        user_elem.send_keys(username)

        # 4， 定位密码；
        pwd_locator = (By.NAME, 'password')
        pwd_elem = self.driver.find_element(*pwd_locator)

        # 5, 输入密码
        pwd_elem.send_keys(pwd)

        # 6, 定位登录按钮；
        # btn_locator = (By.XPATH, "//button[@class='btn btn-special']")
        btn_elem = self.driver.find_element(*self.btn_locator)

        # 7,点击登录按钮；
        btn_elem.click()

    def get_error_msg(self):
        """获取错误信息"""
        error_info_locator = (By.XPATH, "//div[@class='form-error-info']")
        error_elem = self.driver.find_element(*error_info_locator)
        return error_elem.text
