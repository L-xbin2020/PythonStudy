class Gun():
    def __init__(self, model, bullet_count):
        self.model = model
        self.bullet_count = bullet_count
        pass

    def __str__(self):
        return "枪的类型为{}，子弹数量为{}".format(self.model, self.bullet_count)

    def shoot(self):
        if self.bullet_count > 0 :
            self.bullet_count -= 1
            print("射击开始")
            print("剩余子弹为{}".format(self.bullet_count))
            return
        pass
        print("没有子弹")

    def add_bullet(self):
        self.bullet_count += 30


class Solder():
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun
        pass

    def fire(self):
        self.gun.shoot()

        pass

    pass


ak = Gun("ak-47", 30)
xm = Solder("小明", ak)
xm.fire()
ak.add_bullet()
print(ak)