def print_line(str1, time):
    print(str1 * time)
    pass


def print_lines(char, time):
    """
    重复打分割线

    :param char:重复的字符
    :param time:重复的次数
    :return:
    """


    row = 0
    while row < 5:
        print_line(char, time)
        row += 1
        pass
    pass


# print_lines()
