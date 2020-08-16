class Cat():

    def __init__(self, new_name):
        self.name = new_name
        print("{}谁来了".format(self.name))

        pass

    def __del__(self):

        print("我去了{}".format(self.name))


# tom是一个全局变量
tom = Cat("Tom")
print(tom.name)

# del 关键字可以删除一个对象
del tom
print("-"*50)
