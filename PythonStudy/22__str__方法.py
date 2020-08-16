class Cat():

    def __init__(self, new_name):
        self.name = new_name
        print("{}谁来了".format(self.name))

        pass

    def __del__(self):
        print("我去了{}".format(self.name))

    def __str__(self):
        return "wowowo"


# tom是一个全局变量
tom = Cat("Tom")
print(tom)
