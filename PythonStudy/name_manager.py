import user2
from user2 import *




while True:
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print()
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("0. 退出系统")

    print("*" * 50)
    user_num = input("请输入序号")
    if user_num == "1":
        user2.userNew()
        continue

    if user_num == "2":
        user_screen()
        continue

    if user_num == "3":
        user_check()
        continue

    if user_num == "0":
        exit()
        break

    pass

