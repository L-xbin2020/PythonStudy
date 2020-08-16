class Cat:
    def __init__(self, name):
        self.name = name
        print("这是初始化方法")
        pass

    def __str__(self):
        return self.name + "==" + "haah"

    pass


tom = Cat("wo")

print(tom)
