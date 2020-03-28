# 导包
import unittest
import logging
from api.login_api import LoginApi
import app
from utils import assert_commen_utils, read_login_data
from parameterized import parameterized

# 创建测试类
class TestLogin(unittest.TestCase):

    # 初始化测试类
    def setUp(self):
        # 实例化登录接口
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 编写测试的函数
    # 登陆成功
    filename = app.BASE_DIR + "/data/login.json"
    @parameterized.expand(read_login_data(filename))
    def test01_login_success(self,casename, jsonData, http_code, success, code, message):
        # 定义请求体
        jsonData = jsonData
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录结果
        logging.info("{}_响应体数据为：{}".format(casename, response.json()))
        # 断言登录的结果：响应状态码、success、code、message的值
        assert_commen_utils(self, response, http_code, success, code, message)
