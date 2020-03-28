# 导包
import unittest
import requests
import logging
import api
import app
from api.emp_api import EmpApiSession
from utils import assert_commen_utils


class TestEmpSession(unittest.TestCase):
    session = None
    @classmethod
    def setUpClass(cls) -> None:
        # 初始化session
        cls.session = requests.Session()
        cls.emp_api_session = EmpApiSession()

    def setUp(self) -> None:
        self.login_url = "http://182.92.81.159/api/sys/login"
        self.emp_url = "http://182.92.81.159/api/sys/user"

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        # 关闭session
        if cls.session:
            cls.session.close()


    def test01_login_success(self):
        # session发送登录接口请求
        jsonData = {"mobile":"13800000002", "password":"123456"}
        response = self.session.post(self.login_url, headers=app.HEADERS, json=jsonData)
        logging.info("登录请求的结果为：{}".format(response.json()))
        # 提取响应数据中的data的值，保存为token
        token = response.json().get("data")


    def test02_add_emp(self):
        # session发送添加员工接口请求
        response = self.emp_api_session.add_emp_session(self.session, "咪咕啦啦6", "15688559989")

        logging.info("添加员工的结果为：{}".format(response.json()))
        # 获取员工id
        app.EMP_ID = response.json().get("data").get("id")
        logging.info("获取EMP_ID的值为：{}".format(app.EMP_ID))
        # 断言响应状态码 success code message 的值
        assert_commen_utils(self, response, 200, True, 10000, "操作成功")


    def test03_query_emp(self):
        # session发送查询员工接口请求
        response = self.emp_api_session.query_emp_session(self.session,app.EMP_ID)
        logging.info("查询员工的结果为：{}".format(response.json()))
        print("cookies:", response.cookies)
        # 断言响应状态码 success code message 的值
        assert_commen_utils(self, response, 200, True, 10000, "操作成功")

    def test04_modify_emp(self):
        # session发送修改员工接口请求
        response = self.emp_api_session.modify_emp_session(self.session, app.EMP_ID, "啦啦咕咕2")
        logging.info("修改员工的结果为：{}".format(response.json()))
        # 断言响应状态码 success code message 的值
        assert_commen_utils(self, response, 200, True, 10000, "操作成功")

    def test05_delete_emp(self):
        # session发送删除员工接口请求
        response = self.emp_api_session.delete_emp_session(self.session, app.EMP_ID)
        logging.info("删除员工的结果为：{}".format(response.json()))
        # 断言响应状态码 success code message 的值
        assert_commen_utils(self, response, 200, True, 10000, "操作成功")