import json
import unittest
from common import httpRequest


class TestDemo(unittest.TestCase):  # 继承unittest.TestCase

    def __init__(self, methodName):
        super(TestDemo, self).__init__(methodName)
        self.case_name = 'TestDemo'
        self.req = httpRequest.HttpRequest()

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('start tearDown of test')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('start setUp of test.')

    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('start tearDownClass of class.')

    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('start setUpClass of class.')

    def test_A(self):
        print('start testcase A')
        self.req.set_url('/api/hotword.json')
        response = self.req.get()
        json_data = json.loads(response.text)
        self.assertEqual(json_data['result']['status']['code'], 0)
        print(response.text)


    def testB(self):
        print('start testcase B')
        self.assertEqual(1, 2)  # 测试用例


