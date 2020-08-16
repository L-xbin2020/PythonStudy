#
# row = 1
#
# while row <=9:
#     col = 1
#     while col<=row:
#
#         print("{}*{}={}".format(row,col,row*col),end="  ")
#
#         col+=1
#         pass
#     print()
#
#     row +=1

# test_list = [1,2,3,4]
#
# a = test_list.remove(1)
# # a = test_list.pop()
#
#
# print(a)
#
# print(test_list)

def sum_number(num):

    if num == 1:
        return num
    return num+sum_number(num-1)

    pass

result = sum_number(5)
print(result)

