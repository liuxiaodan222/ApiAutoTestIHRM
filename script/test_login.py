# 导包
import unittest
import logging
from api.login_api import LoginApi
import app
from utils import assert_commen_utils


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
    def test01_login_success(self):
        # 定义请求体
        jsonData = {"mobile": "13800000002", "password": "123456"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录结果
        logging.info("响应体数据为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message的值
        assert_commen_utils(self, response, 200, True, 10000, "操作成功！")

    # 密码错误
    def test02_password_is_error(self):
        # 定义请求体
        jsonData = {"mobile": "13800000002", "password": "1234567"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录结果
        logging.info("响应体数据为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message的值
        assert_commen_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 账号不存在
    def test03_mobile_is_not_exist(self):
        # 定义请求体
        jsonData = {"mobile": "13900000002", "password": "123456"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录结果
        logging.info("响应体数据为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message的值
        assert_commen_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 输入的手机号码有英文字符串
    def test04_mobile_has_eng(self):
        # 定义请求体
        jsonData = {"mobile": "1380000A0X2", "password": "123456"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录结果
        logging.info("响应体数据为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message的值
        assert_commen_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 手机号码有特殊字符
    def test05_mobile_has_special(self):
        # 定义请求体
        jsonData = {"mobile": "1380000*0}2", "password": "123456"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录结果
        logging.info("响应体数据为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message的值
        assert_commen_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 手机号码为空
    def test06_mobile_is_empty(self):
        # 定义请求体
        jsonData = {"mobile": "", "password": "123456"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录结果
        logging.info("响应体数据为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message的值
        assert_commen_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码为空
    def test07_password_is_empyt(self):
        # 定义请求体
        jsonData = {"mobile": "13800000002", "password": ""}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录结果
        logging.info("响应体数据为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message的值
        assert_commen_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 多参 - 多出1个参数
    def test08_more_params(self):
        # 定义请求体
        jsonData = {"mobile": "13800000002", "password": "123456", "sign":"1234"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录结果
        logging.info("响应体数据为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message的值
        assert_commen_utils(self, response, 200, True, 10000, "操作成功！")
    # 少参 - 缺少mobile
    def test09_less_mobile(self):
        # 定义请求体
        jsonData = {"password": "123456"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录结果
        logging.info("响应体数据为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message的值
        assert_commen_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 少参 - 缺少password
    def test10_less_password(self):
        # 定义请求体
        jsonData = {"mobile": "13800000002"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录结果
        logging.info("响应体数据为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message的值
        assert_commen_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 无参
    def test11_none_params(self):
        # 定义请求体
        jsonData = None
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录结果
        logging.info("响应体数据为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message的值
        assert_commen_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")

    # 错误参数 - 输入错误的参数
    def test12_params_is_error(self):
        # 定义请求体
        jsonData = {"mboile": "13800000002", "password": "123456"}
        # 利用封装的登录接口，发送登录请求
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录结果
        logging.info("响应体数据为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message的值
        assert_commen_utils(self, response, 200, False, 20001, "用户名或密码错误")
