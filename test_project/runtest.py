# -*- coding: utf-8 -*-
# @Time    : 2018/3/30 15:33
# @Author  : Josie

import unittest,time
from HTMLTestRunner import HTMLTestRunner

# 加载测试文件
from unittest_frame.test_project.test_case import testbaidu,testyoudao

"""
# 构造测试集
suite = unittest.TestSuite()

suite.addTest(testbaidu.MyTest("test_baidu"))
suite.addTest(testyoudao.MyTest("test_youdao"))

if __name__ == "__main__":
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
"""

#--------------- 项目集成测试报告--------------
# 指定测试用例为当前文件夹下的test_case目录
test_dir = "D:/PycharmProjects/unittest_frame/test_project/test_case"
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")

if __name__ == "__main__":

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_dir + "./" + now + "result.html"
    # import pdb;pdb.set_trace()
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况：")
    runner.run(discover)
    fp.close()