class A():
    def test(self):
        print("test--A")
        pass

    def demo(self):
        print("demo--A")
        pass
    pass


class B():
    def test(self):
        print("test--B")
        pass

    def demo(self):
        print("test--B")
        pass

    pass


class C(B,A):
    pass


# 创建子类
c = C()
c.test()
c.demo()

# 确定C类对象调用方法的顺序
print(C.mro())