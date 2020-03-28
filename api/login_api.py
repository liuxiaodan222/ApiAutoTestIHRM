

import requests

# 定义封装登录接口的类
class LoginApi:
    def __init__(self):
        # ihrm登录接口url
        self.login_url = "http://182.92.81.159/api/sys/login"

    def login(self, jsonData, headers):
        response = requests.post(url=self.login_url, json = jsonData, headers = headers)
        return  response


if __name__ == '__main__':
    login_api = LoginApi()
    jsonData = {"mobile":"13800000002", "password":"123456"}
    headers = {"Content-Type":"application/json"}
    response = login_api.login(jsonData, headers)
    print("响应数据为：", response.json())