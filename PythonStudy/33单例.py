class MUsicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None

    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性师范是空对象
        if cls.instance is None:
            # 2.调用父类的方法，为第一对象分配空间
            cls.instance = super().__new__(cls)
            # 3.放回类属性保存的对象引用
            return cls.instance
        return cls.instance

    def __init__(self):

        # 1.判断是否执行过初始化动作
        if MUsicPlayer.init_flag:
            return
        print("初始化动作")
        MUsicPlayer.init_flag = True

    pass


player1 = MUsicPlayer()
print(id(player1))
player2 = MUsicPlayer()
print(id(player2))
