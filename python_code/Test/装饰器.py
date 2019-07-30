user_status = False

def login(auth_type):
    def outer(func):
        def inner(*style,**kwargs):
            while True:
                _username = "Alex"
                _password = "123abc"
                global user_status
                if user_status == False:
                    user = input("user:")
                    psw = input("password:")
                    if _username == user and _password == psw:
                        print("登录成功!")
                        user_status = True
                    else:
                        print("用户名后密码输入错误！")
                else:
                    print("用户已登录，验证通过！")
                if user_status:
                    func(*style,**kwargs)
                    break
        return inner
    return outer

def anhui():
    print("----安徽----")
@login
def shanghai(style):
    print("----上海----",style)
@login("qq") # ==beijing = login(beijing)
def beijing(style):
    print("----北京----",style)
@login("wx")
def shenzhen():
    print("----深圳----")
# beijing = login(beijing) #返回inner的地址传递给beijing
# shanghai = login(shanghai)


beijing("你好")