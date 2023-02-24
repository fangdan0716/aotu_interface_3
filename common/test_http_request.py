import unittest
from common.http_request import HttpRequest
from common.do_excel_new import DoExcel
from ddt import ddt,data
from common.read_conf import ReadConfig
from common.my_log import MyLog
from conf import project_path


test_data=DoExcel(project_path.test_data_path,"Sheet1").read_excel()

logger=MyLog()
COOKIE=None  #全局变量
IP = ReadConfig().read_config(project_path.http_conf_path, "HTTP", 'ip')
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        self.write=DoExcel(project_path.test_data_path, "Sheet1")
        # print("开始执行测试用例!!!")
        logger.info("开始执行测试用例!!!")

    @data(*test_data)
    def test_http_request(self,a):
        # print("测试数据是",a)
        # print("目前正在执行第%s条用例"%a[0])
        logger.info("测试数据是:{0}".format(a))
        logger.info("目前正在执行第%s条用例"%a[0])
        global COOKIE
        res=HttpRequest(IP + a[4],(a[5])).http_request(a[3],cookies=COOKIE)
        #参数
        mobilePhone=a[5]["mobilephone"]
        if res.cookies!={}:
            COOKIE=res.cookies
        print(res.json())
        from common.do_mysql import DbInfo
        config = eval(ReadConfig().read_config(project_path.datebae_conf_path, "DATABASE", 'config'))
        t = DbInfo(config)
        sql = 'select * from member where MobilePhone ="%s"; '%mobilePhone

        res = t.get_data(sql, 1)
        if res != None:
            print("可以注册成功")
        else:
            print("手机号已存在")
        expect = eval(a[6])
        try:
            self.assertEqual(expect['code'], res.json()['code'])
            result = 'pass'

        except AssertionError as e:
            print("报错信息是%s" %e)
            result = 'fail'

            raise e
            # 写入数据
        finally:
            self.write.write_excel(a[0] + 1, str(res.json()), result)



    def  tearDown(self):
        # print("结束执行测试用例!!!")
        logger.info("结束执行测试用例!!!")



