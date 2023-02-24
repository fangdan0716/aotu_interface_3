from common.test_http_request import TestHttpRequest
import time
import unittest
import HTMLTestRunnerNew
from common.send_email import SendMail
from conf import project_path

#TestSuite()
suite=unittest.TestSuite()

#加载测试用例 TestLoader()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
# MyLog().info(suite)

import os
now = time.strftime('%Y-%m-%d_%H_%M_%S')
file_path='test'+now+'.html'

#执行测试用例 ，生成测试报告
with open(file_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title=u"测试报告",description=None,tester=u"测试")
    runner.run(suite)


    # # 发送邮件
    host = 'smtp.qq.com'
    post = 456
    sender = '272392324@qq.com'  # 发送者
    passwd = 'ntuhrxhouhhcbjfa'
    receivers = ['272392324@qq.com']  # 接收者,'1414991281@qq.com','204893985@qq.com'
    subject = '测试报告结果'  # 邮件主题
    from conf import project_path
    file = project_path.email_path_log
    s = SendMail()
    s.send_email_txt(host,456,sender,passwd,receivers,subject,file)
    s.send_mail_html(host,456,sender,passwd,receivers,subject,file)

#common  放置公共内容
#conf 放置配置文件
#public 放置公共代码
#test_data 放置测试数据
#result
# test_result  放置测试结果
# test_report 放置测试报告
# image 放置测试截图
#source
# test_xx  放置不同接口的测试代码
