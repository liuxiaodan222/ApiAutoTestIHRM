import unittest
import time

from HTMLTestRunner_PY3 import HTMLTestRunner

import app
from script.test_emp2 import TestEmplyoee
from script.test_login_params import TestLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmplyoee))

# report_name = app.BASE_DIR + "/report/ihrm_{}.html".format(time.strftime("%Y%m%d_%H%M%S"))
report_name = app.BASE_DIR + "/report/ihrm.html"
with open(report_name, "wb") as f:
    runner = HTMLTestRunner(stream=f, verbosity=2, title="IHRM人力资源管理系统", description="HTMLTestRunner_PY3版本报告")
    runner.run(suite)
