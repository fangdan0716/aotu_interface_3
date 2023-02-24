import unittest
from common.http_request import HttpRequest
from common.do_excel import DoExcel
from ddt import ddt,data
from common.read_conf import ReadConfig
from common.my_log import MyLog
from conf import project_path
test_data=DoExcel("D:\\python3.4\\pycharm_project\\lemon\\auto_interface_case_2\\test_data\\test.xlsx","Sheet1").read_excel()
a=test_data[1]

b=eval(a[5])
print(b)
print(type(b))
res = HttpRequest(a[4], eval(a[5])).http_request(a[3])






