# alien_color = "yellow"
# if alien_color == "yellow":
#     print("恭喜你获得5点")
#     pass
# elif alien_color == "green":
#     print("恭喜玩家获得10点")
# else:
#     print("恭喜玩家获得20点")

# age = int(input("请输入您的年龄"))
# if age < 2:
#     print("他是婴儿")
# elif 2 < age < 4:
#     print("他正蹒跚学步")
# elif 4 < age < 13:
#     print("他是儿童")
# elif 13 < age < 20:
#     print("他是青少年")
# elif 20 < age < 65:
#     print("他是成年人")
# elif age > 65:
#     print("他是老年人")

# admin_name = ["lucy","jack","morning","green","yellow","admin"]
# login_name = input("请输入您登陆的名字")
# if not admin_name:
#     print("We need to find some users!")
# if login_name == "admin":
#     print("Hello admin,would you like to see status report?")
# else:
#     print("Hello Eric,thank you for logging iin again")


current_users = ["lucy","jack","morning","green","yellow","admin"]
new_users = ["Lucy","jack","green","afternoon","hello"]
for new_name in new_users:
    if new_name in current_users:
        print(new_name+"用户名已存在，请重新输入")
    elif new_name.lower() in current_users:
        print(new_name.lower()+"已经存在，请重新输入")
        print(new_name+"用户名未被使用")
