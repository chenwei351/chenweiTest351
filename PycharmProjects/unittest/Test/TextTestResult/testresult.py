# -*- encoding:utf-8 -*-
#测试结果

import  unittest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['testcase.Test_Object']))

    with open('1.txt','a') as  f:
        runner = unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(suite)