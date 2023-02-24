import random
import time

import requests
import json
class HttpRequest:
    def __init__(self,url,param):
        self.url=url
        self.param=param


    def http_request(self,method,headers=None):
        if method.upper()=="GET":
            res=requests.get(self.url,self.param,headers=headers)

        elif method.upper()=="POST":
            res=requests.post(self.url,self.param,headers=headers)

        else:
            print("请求的方式不存在")

        return res




if __name__ == '__main__':
    uuid =time.time()
    score = random.randint(1,100)

    startDate =time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    header = {"Authorization": "", "Content-Type": "application/json"}
    tice = 'https://yuntiyu-api.dream-sports.cn/tice'
    tice_parm = {
        "uuid" : uuid,
        "testUnicode": "e36cb57540404120b041653f3bc44337",
        "testerId": "${testerId}",
        "itemId": 17,
        "score": score,
        "startDate": startDate,
        "endDate": startDate}
