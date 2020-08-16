class Women():
    def __init__(self,name,age):
        self.name = name
        self.__age = age
        pass

    def secret(self):
        print("name{},age{}".format(self.name,self.__age))

    pass



xf = Women("小芳",18)
print(xf.name)
# 私有属性是不能给外界访问
# print(xiao_feng.age)
# print(xf.age)
# 私有方法  是不能给外界访问
# xf.secret()