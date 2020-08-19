try:
    # 提示用户输入一个整数
    num = int(input("int"))

    # 使用8除以用户输入的数字
    result = 8/num

    print(result)

except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("请输入正确的值")
except Exception as result:
    print("未知错误{}".format(result))
else:
    print("尝试成功") 
finally:
    print("无论是否成功都执行")