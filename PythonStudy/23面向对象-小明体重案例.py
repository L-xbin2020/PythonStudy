class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        pass

    def __str__(self):
        return "{}的体重为{}".format(self.name, self.weight)

    def run(self):
        self.weight -= 0.5
        pass

    def eat(self):
        self.weight += 1
        pass


xm = Person("小明",75.0)

xm.run()
print(xm)
xm.eat()
print(xm)

