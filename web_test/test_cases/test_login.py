import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import ddt, data

from web_test.datas import login_data_error
from web_test.pages.login_page import LoginPage


@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    #
    # def setUp(self) -> None:
    #     self.driver=webdriver.Chrome()
    #     self.driver.implicitly_wait(10)
    #
    #
    # def tearDown(self) -> None:
    #     self.driver.quit()

    @data(*login_data_error)
    def test_login_username_emply(self, test_info):
        # 预期结果
        expected = test_info["expected"]
        # 实际结果
        LoginPage(self.driver).login(test_info["mobile"], test_info["pwd"])
        # 断言
        res = LoginPage(self.driver).get_error_msg()
        assert res == expected

    def get_error_msg(self):
        elem_error = self.driver.find_element(By.XPATH, "//div[text()='请输入手机号']")
