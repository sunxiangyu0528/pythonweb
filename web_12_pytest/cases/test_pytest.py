"""pytest 发现测试用例的规则。

pytest 安装：
pip install pytest.

模块规则：test_开头 或者 _test.py 结尾。
类规则：Test
函数名称：test_开头


pytest 不一定要写 类，可以单独以函数的形式存在。


测试用例如何发现的：
pytest 命令会收集运行 pytest 指令的当前目录下所有符合规则的函数。

pytest 命令执行方式：
1， pycharm 右击运行。pytest运行当前的测试用例模块
2,  命令行。  在 cmd 当中在指定的目录下运行 pytest, 就能将当前目录下所有符合规则的用例收集。包括子目录
3， python 函数方式运行


跑冒烟用例。
pytest -m "标签名"
取消警告信息：
新建 pytest.ini 文件：添加
markers = smoke

同时运行多个标签：
pytest -m "login and smoke"
只能使用双引号，不能使用单引号


用例排序：
1， 从上到下执行。而 unittest是根据ascii编码


pytest 第三方库，虽然说功能强大。容易出现版本和 python版本不兼容的情况。
unittest 不存在不兼容情况。
"""


# class TestAdd:
#
#     def test_add(self):
#         pass
import pytest


@pytest.mark.smoke
def test_add():
    pass

def test_min():
    pass

