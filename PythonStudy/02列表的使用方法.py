name_list = ["张三","lisi","wangwu"]

# 1.取值和取索引值

print(name_list[2])

print(name_list.index("wangwu"))
# 2.修改
name_list[1] = "李四"
# 3.添加
name_list.append("ahah")
# 在指定的索引位置插入值或数据
name_list.insert(1,"wobuhi")
print(name_list)

temp_list = ["xiaohong","xiaoming"]
name_list.extend(temp_list)
print(name_list)

# 删除
# remvoe方法可以从列表中删除指定元素
name_list.remove("wangwu")
# pop方法默认可以吧列表中最后一个元素删除
name_list.pop()
# pop可以删除指定索引元素
name_list.pop(3)
print(name_list)
# clear清空列表
name_list.clear()

print(name_list)

