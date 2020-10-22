import Python编程从入门到实践.class_study as lei


class IceCreamStand(lei.Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def description_ice(self):
        print(self.flavors)
        pass


ice = IceCreamStand("jjj","shaya",['wobu'])
ice.description_ice()