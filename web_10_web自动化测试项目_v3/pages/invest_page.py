from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class InvestPage:

    # 投标输入框
    bid_input_locator = (By.XPATH, "//input[@class='form-control invest-unit-investinput']")
    bid_btn_locator = (By.XPATH, "//button[@class='btn btn-special height_style']")
    # 投标成功元素
    bid_success_msg_locator = (By.XPATH, "//div[@class='layui-layer-content']//div[@class='capital_font1 note']")

    def __init__(self, driver: Chrome ):
        self.driver = driver

    def get_bid_input(self):
        """获取投标输入框元素"""
        e = self.driver.find_element(*self.bid_input_locator)
        return e

    def get_bid_btn(self):
        """获取投标按钮元素"""
        e = self.driver.find_element(*self.bid_btn_locator)
        return e

    def bid(self, money):
        """投标"""
        self.get_bid_input().send_keys(money)
        self.get_bid_btn().click()

    def get_bid_success(self):
        e = self.driver.find_element(*self.bid_success_msg_locator)
        return e


