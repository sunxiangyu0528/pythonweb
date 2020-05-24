from selenium.webdriver.common.by import By


class HomePage:
    # 首页的账号
    user_locator = (By.XPATH, "//a[@href='/Member/index.html']")
    # 首页投标按钮
    invest_locator = (By.XPATH, "//div[@class='text-center']//a[@class='btn btn-special']")

    def __init__(self, driver):
        self.driver = driver

    def get_user_info(self):
        """获取账号信息"""
        e = self.driver.find_element(*self.user_locator)
        return e.text

    def get_invest_btn(self):
        """获取投标按钮"""
        e = self.driver.find_element(*self.invest_locator)
        return e
