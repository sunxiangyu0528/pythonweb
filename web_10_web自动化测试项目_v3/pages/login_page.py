"""

"""

from selenium.webdriver.common.by import By
from web_10_web自动化测试项目_v3.config import Setting


class LoginPage:
    """登录页面"""
    url = '/Index/login.html'

    user_locator = (By.NAME, 'phone')
    pwd_locator = (By.NAME, 'password')
    btn_locator = (By.XPATH, "//button[@class='btn btn-special']")
    error_info_locator = (By.XPATH, "//div[@class='form-error-info']")
    invalid_info_locator = (By.CLASS_NAME, "layui-layer-content")

    def __init__(self, driver):
        self.driver = driver

    def get(self):
        """访问登录页面"""
        login_url = Setting.host + self.url
        self.driver.get(login_url)

    def login(self, username, pwd):
        """登录操作"""
        self.get()

        # 定位用户名
        user_elem = self.driver.find_element(*self.user_locator)
        # 3， 输入用户名；
        user_elem.send_keys(username)

        # 4， 定位密码；
        pwd_elem = self.driver.find_element(*self.pwd_locator)
        # 5, 输入密码
        pwd_elem.send_keys(pwd)

        # 6, 定位登录按钮；
        btn_elem = self.driver.find_element(*self.btn_locator)
        # 7,点击登录按钮；
        btn_elem.click()

    def get_error_msg(self):
        """获取错误信息"""
        error_elem = self.driver.find_element(*self.error_info_locator)
        return error_elem.text

    def get_invalid_msg(self):
        """获取未授权信息"""
        invalid_elem = self.driver.find_element(*self.invalid_info_locator)
        return invalid_elem.text
