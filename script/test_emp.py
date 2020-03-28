# 导包
import unittest
import app
import logging

from api.emp_api import EmpApi
from api.login_api import LoginApi
import requests
from utils import assert_commen_utils

# 创建测试类



class TestEmplyoee(unittest.TestCase):
    # 初始化
    def setUp(self) -> None:
        # 实例化登录接口
        self.login_api = LoginApi()
        # 实例化员工接口
        self.emp_api = EmpApi()
        self.emp_url = "http://182.92.81.159/api/sys/user"

    def tearDown(self) -> None:
        pass

    # 编写测试员工增删改查的案例
    def test01_emp_operation(self):
        # 登录接口
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"}, app.HEADERS)
        jsonData = response.json()
        logging.info("打印登录接口响应体数据：{}".format(jsonData))
        # 获取响应体中的令牌数据
        token = jsonData.get("data")
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        logging.info("员工模块接口请求头为：{}".format(headers))

        # 添加员工
        response = self.emp_api.add_emp("珠穆拉囊tyy", "18985641562", headers)
        # 打印添加的结果
        logging.info("添加员工的结果为：{}".format(response.json()))
        #   获取添加员工返回的json数据
        add_result = response.json()
        # 提取员工id，保存到变量中
        emp_id = add_result.get("data").get("id")
        logging.info("获取到的员工id为：{}".format(emp_id))
        # 断言
        assert_commen_utils(self, response, 200, True, 10000, "操作成功")

        # 查询员工
        # 发送查询员工接口请求
        response = self.emp_api.query_emp(emp_id, headers)
        # 打印查询结果
        logging.info("查询员工的结果为：{}".format(response.json()))
        # 断言
        assert_commen_utils(self, response, 200, True, 10000, "操作成功")

        # 修改员工
        # 发送修改员工接口请求
        response = self.emp_api.modify_emp(emp_id, "珠穆拉拉", headers)
        logging.info("修改员工的结果为：{}".format(response.json()))
        # 断言
        assert_commen_utils(self, response, 200, True, 10000, "操作成功")

        # 删除员工
        delete_emp_url = self.emp_url + "/" + emp_id
        logging.info("删除员工接口的url为：{}".format(delete_emp_url))
        # 发送修改员工接口请求
        response = self.emp_api.delete_emp(emp_id, headers)
        logging.info("删除员工的结果为：{}".format(response.json()))
        # 断言
        assert_commen_utils(self, response, 200, True, 10000, "操作成功")