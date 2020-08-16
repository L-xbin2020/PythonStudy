class HouseItem():
    def __init__(self, name, area):
        self.name = name
        self.area = area
        pass

    def __str__(self):
        return "{}的占地面积是{}".format(self.name, self.area)

    pass


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []
        pass

    def __str__(self):
        return "户型{}，总面积{}，剩余面积{}，家具{}" \
            .format(self.house_type, self.area,
                    self.free_area, self.item_list)

    def add_item(self, item):
        print("要添家{}".format(item))
        # 1.判断家具的面积
        if item.area > self.free_area:
            print("{}的面积太大".format(item.name))

            return
        # 2.将家具的名称添加到列表中
        self.item_list.append((item.name))
        # 3.计算剩余面积
        self.free_area -= item.area

#




# 1.创建家具
bed = HouseItem("席梦思", 40)
chest = HouseItem("衣柜", 20)
table = HouseItem("餐桌", 1.5)

# 2.创建房子对象
my_house = House("两室一厅",60)

my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)

print(my_house)
