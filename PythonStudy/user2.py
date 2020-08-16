
user_list =[{'name': '王五', 'phone': '10086', 'qq': '123', 'email': '123'},
            {'name': '小明', 'phone': '10086', 'qq': '123', 'email': '123'}
            ]
def userNew():
    user_name = input("姓名")
    user_phone = input("电话")
    user_qq = input("qq")
    user_email = input("邮箱")

    user_dict = {}
    user_dict["name"] = user_name
    user_dict["phone"] = user_phone
    user_dict["qq"] = user_qq
    user_dict["email"] = user_email

    user_list.append(user_dict)
    pass
def user_screen():
    print(user_list)
    pass
def user_check():
    user_name = input("请输入您要查询的名字")
    for dicts in user_list:

        if user_name == dicts["name"]:
            print(dicts)
            print("修改请输入1/删除请输入0/退出请输入2")
            user_num2 = input("请输入数字")
            if user_num2 == "1":
                user_alter(dicts)
                pass
            if user_num2 == "0":
                pass
            if user_num2 == "2":
                pass
            break
    else:
        print("无")



def user_alter(dics):
    user_name = input("姓名")
    if user_name != "":
        dics["name"] = user_name
        pass













if __name__ == "__main__":
    # userNew()
    # print(user_list)
    # pass
    user_check()

