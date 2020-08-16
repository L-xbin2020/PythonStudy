# 全局变量
num = 10

def demo1():
    # 希望膝盖全局变量的值 - 使用global 声明一下变量即可
    # global 关键字会告诉解释器后面的变量是一个全局变量
    # 在使用赋值语句是，就不会创建局部变量
    global  num

    num = 99

    print("demo1 ==> %d"%num)
    pass
def demo2():
    num = 9
    print("demo2 ==>%d"%num)
    pass
demo1()
demo2()