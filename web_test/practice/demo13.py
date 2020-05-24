import unittest
import pytest
from selenium import webdriver


class TestDemo(unittest.TestCase):


    def test_01(self):
        print("111")

        self.assertEqual(1,1)


# if __name__="__main__":


    pytest.main()
