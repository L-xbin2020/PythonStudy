def input_password():

    # 1.提供用户输入密码
    pwd = input("输入密码")

    # 2.判断密码长度
    if len(pwd) >= 8:
        return pwd

    # 3.如果 <8 主动抛出异常
    print("主动抛出异常")

    ex = Exception("密码不够长")

    raise ex


try:
    input_password()
except Exception as result:
    print(result)
    pass