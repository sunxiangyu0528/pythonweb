from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_user_info(self):
        """获取账号信息"""
        user_locator = (By.XPATH, "//a[@href='/Member/index.html']")
        e = self.driver.find_element(*user_locator)
        return e.text
