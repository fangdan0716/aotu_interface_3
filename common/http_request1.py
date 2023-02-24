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
    header ={"client-key":"mini-yunketang-dev-b","api-version":"6","Content-Type":"application/json"}
    getValidCode='https://yunketang-api.dream-sports.cn/dev/sms/getValidCode'
    login='https://yapi.lovedabai.com/mock/366/user/login'
    user_child_list='https://yunketang-api.dream-sports.cn/dev/user/child/list'
    getValidCode_param={"mobile" :"13088888881","function" : "login"}
    login_param={"type" : "mobile","code" : "8624","mobile":"13100678853"}


    #注册
    # res_register=requests.get(getValidCode,getValidCode_param,cookies=None)
    # print(res_register.json())
    #发送短信
    res_reg=HttpRequest(getValidCode,param=json.dumps(getValidCode_param)).http_request('post',headers=header)
    print(res_reg.json())
    # 登录
    login_reg = HttpRequest(login, param=json.dumps(login_param)).http_request('post', headers=header)
    res_json =login_reg.json()
    print(res_json)
    token1 = res_json['result']['token']
    print(token1)
    # header["X-Auth-Token"] = token1
    # # 登录
    # uchild_list_res = HttpRequest(user_child_list, param=None).http_request('post', headers=header)
    # print(uchild_list_res.json())

    print(time.time())

    # {
    #     "serverTime": 1660109731833,
    #     "result": [
    #         {
    #             "id": 253,
    #             "nickName": "dahuakeji",
    #             "roleCode": "ROLE_TEACHER",
    #             "schoolName": "dahuakeji",
    #             "schoolInnerId": 407
    #         },
    #         {
    #             "id": 254,
    #             "avatar": "http://pic-dev.dream-sports.cn/statics/avatar/2022/08/08/de1631bb94164ec3a959a40a0e10815b.jpeg",
    #             "gender": "M",
    #             "nickName": "芳芳",
    #             "roleCode": "ROLE_STUDENT",
    #             "schoolName": "dahuakeji",
    #             "gradeName": "一年级",
    #             "teamNumerName": "1班",
    #             "schoolInnerId": 63259
    #         },
    #         {
    #             "id": 255,
    #             "avatar": "http://pic-dev.dream-sports.cn/statics/avatar/2022/08/08/eaa8b101a2e341b3824bec975245589c.jpg",
    #             "gender": "F",
    #             "nickName": "小葛",
    #             "roleCode": "ROLE_STUDENT",
    #             "schoolName": "dahuakeji",
    #             "gradeName": "三年级",
    #             "teamNumerName": "1班",
    #             "schoolInnerId": 63260
    #         },
    #         {
    #             "id": 256,
    #             "avatar": "http://pic-dev.dream-sports.cn/statics/avatar/2022/08/09/397daaa2142b4d0d81a265bebe1bd89b.jpg",
    #             "gender": "M",
    #             "nickName": "刘巍",
    #             "roleCode": "ROLE_STUDENT",
    #             "schoolName": "dahuakeji",
    #             "gradeName": "六年级",
    #             "teamNumerName": "2班",
    #             "schoolInnerId": 63261
    #         },
    #         {
    #             "id": 257,
    #             "avatar": "http://pic-dev.dream-sports.cn/statics/avatar/2022/08/09/03f46a1cd6e34f069adaff85fba40e13.jpg",
    #             "gender": "F",
    #             "nickName": "潇潇",
    #             "roleCode": "ROLE_STUDENT",
    #             "schoolName": "dahuakeji",
    #             "gradeName": "三年级",
    #             "teamNumerName": "1班",
    #             "schoolInnerId": 63263
    #         },
    #         {
    #             "id": 258,
    #             "avatar": "http://pic-dev.dream-sports.cn/statics/avatar/2022/08/09/0c6f37dae60c4b66aa210fdb221dc895.jpeg",
    #             "gender": "M",
    #             "nickName": "喵喵",
    #             "roleCode": "ROLE_STUDENT",
    #             "schoolName": "dahuakeji",
    #             "gradeName": "三年级",
    #             "teamNumerName": "1班",
    #             "schoolInnerId": 63262
    #         }
    #     ]
    # }
    #










