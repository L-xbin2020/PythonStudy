# 7-4
# while True:
#     peiliao = input("请输入您需要的配料")
#
#     if peiliao == "quit":
#         break
#     print("我们将在披萨中加入您的配料" + peiliao)
#
#     pass

# while True:
#     age = int(input("请输入您的年龄"))
#     if age <= 3:
#         print("免票")
#     if 3< age < 12:
#         print("10美元")
#     if age >= 12:
#         print("15美元")
#     pass

# 7-8
sandwich_orders = ["lucy","jack","mary","pastrami"]
pastrami_num = 3
finished_sandwiches = []
while sandwich_orders:
    for current_sandwich in sandwich_orders:

        if current_sandwich == "pastrami":

            if pastrami_num <= 0:
                sandwich_orders.remove("pastrami")
                continue
            pastrami_num -= 1
        print("I made " + current_sandwich + " sandwich")
        if current_sandwich == "pastrami":
            finished_sandwiches.append(current_sandwich)
            continue
        else:
            sandwich_orders.remove(current_sandwich)
        finished_sandwiches.append(current_sandwich)
    pass

for name in finished_sandwiches:
    print(name)
