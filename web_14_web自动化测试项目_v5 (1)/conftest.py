"""conftest.py 文件名称是固定的。

统一存放 fixture 的地方。
"""
import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def get_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
