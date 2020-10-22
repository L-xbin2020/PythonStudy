# 3-1
name = ["lucy","jack","xiaobin"]
# for a in name:
#     print(a)
#     pass

# 3-2
for a in name:
    print("Holle,"+a)
    pass
print("*" * 50)

# 3-4
jiabin = ["刘备","张飞","吕布"]
print(jiabin)
print(jiabin[2] + "无法赴约")
jiabin[2] = "关羽"
print(jiabin)
print("将邀请更加多人")
jiabin.insert(0,"诸葛亮")
jiabin.insert(1,"周瑜")
jiabin.append("曹操")
print(jiabin)
print("减少人数")
print("*"*60)
for a in range(len(jiabin)):
    if len(jiabin) > 2 :
        jiabin.pop()

for list_name in jiabin:
    print(list_name + "," +"依旧在被邀请的名单中")

del jiabin[0]
print(jiabin)
del jiabin[0]


if not jiabin:
    print("列表为空")
    pass

print(jiabin)
