for num in [1,2,3]:
    print(num)
    if num==2:
        break
    pass
else:
    # 如果循环体内部使用了break退出了循环
    # else 下方的diamante就不被执行
    print("会执行吗")

print("循环结束")
