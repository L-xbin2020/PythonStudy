import card_tool
# 无限循环，有用户主动决定什么时候退出
while True:
    # 显示功能菜单
    card_tool.show_menu()
    action_str = input("请选择希望执行的操作")
    print("您选择的操作是【%s】" % action_str)
    # 1,2,3 针对名片的操作
    if action_str in ["1","2","3"]:
        # 新增名片
        if action_str == "1":
            card_tool.new_card()
            pass
        # 显示全部
        if action_str == "2":
            card_tool.show_all()
            pass

        # 查询名片
        if action_str == "3":
            card_tool.search_card()
            pass

        pass
    # 0 退出系统
    elif action_str == "0":
        # 如果在开发程序是，不希望like编写内部分支的代码
        # 可以使用pass关键字
        # 程序运行时,pass关键字不会执行任何操作
        print("欢迎使用")
        break
        # pass

    # 其他内容输入错误,需要提示用户
    else:
        print("您输入的不正确，请 重新选择")
