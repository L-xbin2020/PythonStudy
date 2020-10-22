# 6-8
# wangcai = {
#     "type" : "中华田园犬",
#     "admin" : "lucy"
# }
# ahuan = {
#     "type" : "金毛",
#     "admin" : "小明"
# }
# pet = [wangcai,ahuan]
# for pet_name in pet:
#     print(pet_name["type"] + "\t" + pet_name["admin"])

# 6-9
# favorite_place = {
#     "小明" : ["北京","上海","广州","深圳"],
#     "小红" : ["重庆","浙江"],
#     "梁" : ["南京","纽约"]
# }
#
# for k,k_place in favorite_place.items():
#
#
#     print(k + "去的地方是",end="")
#     print(k_place)

# 6-11
cities = {
    "广州" : {
        "country" : "中国",
        "population" : "20000",
        "description" : "是中国一线城市"
    },
    "纽约" : {
        "country" : "美国",
        "population" : "233000",
        "description" : "是美国城市"

    }
}

for k,k_detain in cities.items():
    print(k,end="\n")
    for k,v in k_detain.items():
        print(k + "\t" + v)
