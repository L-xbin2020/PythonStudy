
def demo(num,num_List):

    print("函数开始")
    # num = num + num
    num += num
    # 列表变量使用 += 不会做相加在赋值的操作
    # 本质上是在调用 extend 方法 
    # num_list = num_list + num_list
    num += num_List

    print(num)
    print(num_List)
    print("函数完成")

    pass


gl_num = 9



