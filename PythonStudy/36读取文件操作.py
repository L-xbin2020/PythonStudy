# 1.打开文件
file = open("README")
# 2.读取文件内容
text = file.read()
print(text)

# 文件指针已经到了末尾，所以第二次text的值为0
print("---"*50)
text = file.read()
print(text)

# 3.关闭文件
file.close()