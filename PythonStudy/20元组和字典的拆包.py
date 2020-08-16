def demo(*args,**kwargs):

    print(args)
    print(kwargs)
    pass

# 元组变量/字典变量
gl_num = (1,2,3)
gl_dict = {"name":"小明","age":18}

# demo(gl_nums,gl_dict)
demo(*gl_num,**gl_dict)
