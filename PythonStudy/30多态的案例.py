class Dog(object):

    def __init__(self,name):
        self.name = name
        pass

    def game(self):
        print("{}蹦蹦跳跳".format(self.name))
        pass

    pass


class XiaoTianDog(Dog):

    def game(self):
        print("{}飞到天上玩".format(self.name))
        pass


class Person(object):

    def __init__(self,name):
        self.name = name

    def game_with_dog(self,dog):
        print("{}和{}快乐的玩耍。。。".format(self.name,dog.name))
        dog.game()

# 创建一个狗对象
# wangcai = Dog("旺财")
wangcai = XiaoTianDog("旺财")
# 创建一个小明对象
xm = Person("小明")
# 让小明调用和狗玩耍的方法
xm.game_with_dog(wangcai)