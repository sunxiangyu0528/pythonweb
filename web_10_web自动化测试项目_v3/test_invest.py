"""投资用例。

前置条件：
1，登录
2，有余额。充值，1， 无法进行web自动化充值。 2， 直接修改数据库； 3，接口充值。4，手工充值
充多少钱？？
1， 每次查看用例你需要投资多少钱，我就充值多少（每次执行用例之前，都需要去充值一次）
2， 先充一个亿。

3，有项目可投


投资流程：
1，首页点击投标。
2， 投标详情页

"""
import unittest
from selenium import webdriver

from web_10_web自动化测试项目_v3.config.user_config import User
from web_10_web自动化测试项目_v3.pages.home_page import HomePage
from web_10_web自动化测试项目_v3.pages.invest_page import InvestPage
from web_10_web自动化测试项目_v3.pages.login_page import LoginPage


class TestInvest(unittest.TestCase):

    def setUp(self) -> None:
        # 登录
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        wait_timeout = 20
        self.driver.implicitly_wait(wait_timeout)
        LoginPage(self.driver).login(User.username, User.pwd)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_invest_success(self):
        """投资成功用例"""
        HomePage(self.driver).get_invest_btn().click()
        InvestPage(self.driver).bid(100)

        self.assertEqual(InvestPage(self.driver).get_bid_success().text, '投标成功！')

        # 要判断余额
        # 坑1：浮点数 断言。丢失精度， 0。1 + 0.2 != 0.3
        # 坑2： 余额之前  - 投资金额 == 之后余
        # BasePage, 截图，log记录， 异常处理