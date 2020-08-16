class HouseItem():
    def __init__(self, name, area):
        self.name = name
        self.area = area
        pass

    def __str__(self):
        return "{}的面积是{}".format(self.name, self.area)

    pass


class House():
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []
        pass

    def __str__(self):
        return "房子是{}，面积为{}，剩余面积{}，家具列表{}". \
            format(self.house_type, self.area,
                   self.free_area, self.item_list)

    def add_item(self, item):
        print("开始添加家具")
        if self.free_area < item.area:
            print("房子面积太大，放不下，房子剩余面积为{}，家具面积为{}".format(self.free_area, item.area))
            return
        self.free_area -= item.area
        self.item_list.append(item.name)


bed = HouseItem("席梦思", 40)
chest = HouseItem("椅子", 10)
table = HouseItem("桌子", 2)
house = House("两室一厅",120)
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
print(house)
