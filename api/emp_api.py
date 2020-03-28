import logging

import requests


# 封装员工接口类
class EmpApi:
    def __init__(self):
        self.emp_url = "http://182.92.81.159/api/sys/user"

    # 添加员工接口
    def add_emp(self, username, mobile, headers):
        jsonData = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-03-16",
            "formOfEmployment": 2,
            "departmentName": "snowsnow",
            "departmentId": "1226092852421177344",
            "correctionTime": "2020-03-15T16:00:00.000Z"
        }
        logging.info("添加员工URL:{}".format(self.emp_url))
        logging.info("添加员工请求头:{}".format(headers))
        logging.info("添加员工请求体:{}".format(jsonData))
        return requests.post(self.emp_url, json=jsonData, headers=headers)
        # return requests.post(self.emp_url, json=jsonData, headers=headers)

    # 查询员工接口
    def query_emp(self, emp_id, headers):
        # 拼接查询员工接口url
        query_emp_url = self.emp_url + "/" + emp_id
        return requests.get(url=query_emp_url, headers=headers)

    def modify_emp(self, emp_id, username, headers):
        # 拼接修改员工接口url
        modify_emp_url = self.emp_url + "/" + emp_id
        jsonData = {"username": username}
        return requests.put(url=modify_emp_url, json=jsonData, headers=headers)

    def delete_emp(self, emp_id, headers):
        # 拼接查询员工接口url
        delete_emp_url = self.emp_url + "/" + emp_id
        return requests.delete(url=delete_emp_url, headers=headers)



class EmpApiSession:
    def __init__(self):
        self.emp_url = "http://182.92.81.159/api/sys/user"

    def add_emp_session(self, session, username, mobile):
        json = {"username": username,
                "mobile": mobile,
                "timeOfEntry": "2020-03-16",
                "formOfEmployment": 2,
                "departmentName": "snowsnow",
                "departmentId": "1226092852421177344",
                "correctionTime": "2020-03-15T16:00:00.000Z"}
        return session.post(url=self.emp_url, json=json)

    def query_emp_session(self, session,emp_id):
        query_emp_url = self.emp_url + "/" + emp_id
        return session.get(url=query_emp_url)

    def modify_emp_session(self, session, emp_id, username):
        modify_emp_url = self.emp_url + "/" + emp_id
        json = {"username":username}
        return session.put(url = modify_emp_url, json=json)

    def delete_emp_session(self, session, emp_id):
        delete_emp_url = self.emp_url + "/" + emp_id
        return session.delete(url=delete_emp_url)