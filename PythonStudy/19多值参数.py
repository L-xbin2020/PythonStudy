# def demo(num,*args,**kwargs):
#     print(num)
#     print(args)
#     print(kwargs)
#
#
#     pass
#
# demo(1,2,3,4,5,name="小明"，age = 18)
#
#
def sum_number(*args):

    num = 0
    for n in args:
        num += n
        pass

    return num
    pass
result = sum_number(1,23,4,5)
print(result)
