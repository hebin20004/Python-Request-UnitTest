import os
import unittest
from common.log import MyLog as Log
import common.HTMLTestRunner as HTMLTestRunner


class RunTC:
    def __init__(self):
        global log, logger
        log = Log.get_log()
        logger = log.get_logger()


    def run(self):
        """
        run test
        :return:
        """
        suite = unittest.TestSuite()  # 创建测试套件
        all_cases = unittest.defaultTestLoader.discover('./testcase', 'test*.py', top_level_dir=None)
        # 找到某个目录下所有的以test开头的Python文件里面的测试用例
        for case in all_cases:
            suite.addTests(case)  # 把所有的测试用例添加进来
        fp = open('res.html', 'wb')
        # 注意:verbosity参数可以控制输出的错误报告的详细程度，只有3个取值
        # 0 (quiet): 只显示执行的用例的总数和全局的执行结果。
        # 1 (default): 默认值，显示执行的用例的总数和全局的执行结果，并对每个用例的执行结果（成功T或失败F）有个标注。
        # 2 (verbose): 显示执行的用例的总数和全局的执行结果，并输出每个用例的详细的执行结果。
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='generated by HTMLTestRunner.', verbosity=2)
        runner.run(suite)

        fp.close()


if __name__ == '__main__':
    obj = RunTC()
    obj.run()
