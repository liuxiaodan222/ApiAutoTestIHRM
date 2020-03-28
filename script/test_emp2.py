# 导包
import unittest
import app
import logging

from api.emp_api import EmpApi
from api.login_api import LoginApi
import requests
from utils import assert_commen_utils,read_emp_data
from parameterized import parameterized

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
        app.HEADERS = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        logging.info("员工模块接口请求头为：{}".format(app.HEADERS))

    # 数据文件路径
    filename = app.BASE_DIR + "/data/emp.json"
    # 参数化
    @parameterized.expand(read_emp_data(filename, "add_emp"))
    def test02_add_emp(self,username, mobile, http_code, success, code, message):
        # 添加员工
        response = self.emp_api.add_emp(username, mobile, app.HEADERS)
        # 打印添加的结果
        logging.info("添加员工的结果为：{}".format(response.json()))
        #   获取添加员工返回的json数据
        add_result = response.json()
        # 提取员工id，保存到变量中
        app.EMP_ID = add_result.get("data").get("id")
        logging.info("EMP_ID的值为：{}".format(app.EMP_ID))
        # 断言
        assert_commen_utils(self, response, http_code, success, code, message)

    def test03_query_emp(self):
        # 查询员工
        # 发送查询员工接口请求
        response = self.emp_api.query_emp(app.EMP_ID, app.HEADERS)
        # 打印查询结果
        logging.info("查询员工的结果为：{}".format(response.json()))
        # 断言
        assert_commen_utils(self, response, 200, True, 10000, "操作成功")

    def test04_modify_emp(self):
        # 修改员工
        # 发送修改员工接口请求
        response = self.emp_api.modify_emp(app.EMP_ID, "珠穆拉拉", app.HEADERS)
        logging.info("修改员工的结果为：{}".format(response.json()))

        # 在断言之前执行数据库操作，否则断言失败会无法执行
        # 导包
        import pymysql
        # 连接数据库
        conn = pymysql.connect(host="182.92.81.159", user="readuser", password="iHRM_user_2019", database="ihrm")
        # 获取游标
        cursor = conn.cursor()

        sql = "select username from bs_user where id={}".format(app.EMP_ID)
        # 打印执行的SQL语句
        logging.info("执行的SQL语句为：{}".format(sql))
        # 执行SQL语句
        cursor.execute(sql)
        result = cursor.fetchone()
        logging.info("执行SQL语句的结果为：{}".format(result))
        # 断言执行结果
        self.assertEqual("珠穆拉拉",result[0])
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()

        # 断言
        assert_commen_utils(self, response, 200, True, 10000, "操作成功")

    def test05_delete_emp(self):
        # 删除员工
        delete_emp_url = self.emp_url + "/" + app.EMP_ID
        logging.info("删除员工接口的url为：{}".format(delete_emp_url))
        # 发送修改员工接口请求
        response = self.emp_api.delete_emp(app.EMP_ID, app.HEADERS)
        logging.info("删除员工的结果为：{}".format(response.json()))
        # 断言
        assert_commen_utils(self, response, 200, True, 10000, "操作成功")