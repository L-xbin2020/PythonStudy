# 1.判断空白字符

space_str = "    \t\n\r"
print(space_str.isspace())
# 2.判断字符串中是否只包含数字
# 1>都不能判断小数   都不可以
# 2>unicode 字符串  后两个可以
# 3>中文数字        最后一个可以

num_str = "二"


print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
