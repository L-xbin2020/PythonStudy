def print_info(name, title,gender=True):
    """

    :param title:职位
    :param name: 班上同学的姓名
    :param gender: True  男生 False
    :return:
    """
    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("{}是{}".format(name, gender_text))
    pass


# 假设班上的同学，男生居多
# 提示：在只多功能缺省参数的默认值是，应该使用最常看见的值作为默认值
print_info("小明")
print_info("小梅", False)

