import requests
class HttpRequest:
    def __init__(self,url,param):
        self.url=url
        self.param=param

    def http_request(self,method,cookies=None):
        if method.upper()=="GET":
            res=requests.get(self.url,self.param,cookies=cookies)

        elif method.upper()=="POST":
            res=requests.get(self.url,self.param,cookies=cookies)

        else:
            print("请求的方式不存在")

        return res




if __name__ == '__main__':

    register='http://119.23.241.154:8080/futureloan/mvc/api/member/register'
    login='http://119.23.241.154:8080/futureloan/mvc/api/member/login'
    recharge='http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'
    register_param={"mobilephone":"18320187020","pwd":"123456123456789012221","regname":"密19"}
    login_param={"mobilephone":"18320187023","pwd":"123456"}
    recharge_param={"mobilephone":"18320187023","amount":500001.00}

    #注册
    # res_register=requests.get(register,register_param,cookies=None)
    # print(res_register.json())
    #实例化注册
    res_reg=HttpRequest(register,register_param).http_request('get')
    print(res_reg.json())


    #登录  cookie是必须登录了之后才会生成的
    # res_login=requests.get(login,login_param,cookies=None)
    # print(res_login.json())
    # cookie=res_login.cookies  #登录请求发出去之后才会查到cookie
    # print(cookie)

    #实例化登录
    res_login=HttpRequest(login,login_param).http_request("post")
    print(res_login.json())
    print(res_login.cookies)


    #充值
    # res_recharge=requests.get(recharge,recharge_param,cookies=None)
    # print(res_recharge.json())
    # print(res_recharge.cookies)


    #实例化充值
    res_rec=HttpRequest(recharge,recharge_param).http_request("post",cookies=res_login.cookies)
    print(res_rec.json())






