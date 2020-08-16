class Cat:
    def eat(self):
        pass
    def drink(self):
        print("喝水".format(self.name))

        pass
    pass


tom = Cat()

# 设置tom属性
# tom.name = "tom"

tom.drink()
tom.eat()
tom.name = "tom"