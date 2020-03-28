# 封装通用断言函数
import json

import app


def assert_commen_utils(self, response, status_code, success, code, message):
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))

# 封装读取数据的函数
def read_login_data(filename):
    result = []
    with open(filename, "r", encoding="utf-8") as f:
        python_data = json.load(f)
        for data in python_data:
            result.append(tuple(data.values()))

        return result


def read_emp_data(filename, interface_name):
    result = []
    with open(filename, "r", encoding="utf-8") as f:
        python_data = json.load(f)
        result.append(tuple(python_data.get(interface_name).values()))

    return result


if __name__ == '__main__':
    # filename = app.BASE_DIR + "/data/login.json"
    # res = read_login_data(filename)
    # print(res)
    # for r in res:
    #     print(r)

    filename = app.BASE_DIR + "/data/emp.json"
    res = read_emp_data(filename, "add_emp")
    print(res)
