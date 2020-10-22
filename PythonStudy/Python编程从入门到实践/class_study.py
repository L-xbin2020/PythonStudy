class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_servd = 500
        pass

    def describe_restaurant(self):
        print(self.restaurant_name+"??"+self.cuisine_type)
        print(self.number_servd)

    def open_restaurant(self):
        print("餐厅正在营业")
    pass

    def set_number_served(self,number):
        self.number_servd += number
    pass


KFC = Restaurant("肯德基","wobuzhidao")

KFC.describe_restaurant()
KFC.open_restaurant()
KFC.set_number_served(55)
KFC.describe_restaurant()
# 9-3
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        pass

    def describe_user(self):
        print(self.first_name+self.last_name)
        print(self.login_attempts)
        pass

    def greet_user(self):
        print("你好啊{}，很高兴认识你".format(self.first_name+self.last_name))
        pass

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

xm = User("li","hua")
xm.describe_user()
xm.greet_user()
xm.increment_login_attempts()
xm.reset_login_attempts()