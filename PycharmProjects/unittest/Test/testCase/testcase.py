# -*- encoding:utf-8 -*-
import time
import  random
import  requests
import  unittest
from test  import  *
from  Test.TestObject.testobject import  *
# 测试用例


class Test_Object(unittest.TestCase):
    def setUp(self):
        pass
    def test_add(self):
        self.assertEqual(3,add(1,2))
        # self.assertEqual(3,add(1,2))

    def test_minus(self):
        self.assertEqual(2,minus(5,3))
        # self.assertEqual(2,minus(4,3))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()