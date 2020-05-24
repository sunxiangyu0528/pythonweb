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
import time
import unittest
import ddt
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from data import login_data_error, login_data_invalid, login_data_success
from pages.home_page import HomePage
from pages.login_page import LoginPage



class TestLogin:

    @pytest.mark.parametrize('test_info', login_data_error)
    @pytest.mark.login
    def test_login_username_empty(self, test_info, get_browser):
        driver = get_browser
        # driver = get_browser
        expected = test_info['expected']
        LoginPage(driver).login(test_info["mobile"], test_info["pwd"])
        error_msg = LoginPage(driver).get_error_msg()
        try:
            assert error_msg == expected
        except AssertionError as e:
            raise e


    # def test_login_invalid_user(self, test_info, init_web):
    #     expected = test_info['expected']
    #     LoginPage(self.driver).login(test_info["mobile"], test_info["pwd"])
    #     invalid_msg = LoginPage(self.driver).get_invalid_msg()
    #     try:
    #         self.assertEqual(invalid_msg, expected)
    #     except AssertionError as e:
    #         raise e

    # @pytest.mark.smoke
    # def test_login_success_user(self, test_info, init_web):
    #     expected = test_info['expected']
    #     LoginPage(self.driver).login(test_info["mobile"], test_info["pwd"])
    #     account_msg = HomePage(self.driver).get_user_info()
    #     try:
    #         assert account_msg == expected
    #     except AssertionError as e:
    #         raise e


