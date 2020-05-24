import unittest
import ddt

lst = [1, 2, 3]
dic = {"userName": "chen"}
tur = (1, 2, 3)
s = {1, 2, 3}


@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(*lst)
    def test_list(self, data):
        print("test_list")
        print(data)
        print("==================")

    @ddt.data(*dic)
    def test_dictionary(self, data):
        print("test_dic")
        print(data)
        print("==================")

    @ddt.file_data("ddt_test001.json")
    def test_file(self, key):
        print(key)

    @ddt.file_data("ddt_test.json")
    @ddt.unpack
    def test_file(self, start, end, value):
        print(start, end, value)


if __name__ == "__main__":
    unittest.main()