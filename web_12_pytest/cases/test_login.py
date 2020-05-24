

# 表明用例类型
import sys
import pytest


# @pytest.mark.success
# @pytest.mark.login
import conf


class TestLogin:
    # pytestmark 固定的类变量
    # pytestmark = [pytest.mark.success, pytest.mark.smoke]

    # @pytest.mark.skip(reason='out-of-date api, api 过时')
    def test_login_error(self):
        print("")
        assert "登录失败" == "登录成功"

    # 测试环境不同。
    # @pytest.mark.skipif( conf.product_host == 'http://www.example.com',  reason='不能在window上面测试')
    def test_login_invalid(self):
        """没有授权"""
        assert "登录失败2" == "登录成功2"

    @pytest.mark.smoke
    def test_login(self):
        assert "登录成功" == "登录成功"




