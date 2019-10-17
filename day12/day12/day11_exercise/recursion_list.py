#    2. 已知有列表:
#     L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#     1) 写一个函数 print_list(lst) 打印出所有的数字
#        print_list(L)  # 打印 3 5 8 10 13 14  ...
#        注: 不要求打印在一行内
#     2) 写一个函数 sum_list(lst) 返回这个列表中所有数字的和
#         print(sum_list(L))  # 106
#     提示:
#       type(x) 可以返回一个变量的类型,可以用is运算符来比较
#       类型
#         如:
#            type(20) is int  # True
#            type([1, 2, 3]) is list  # True

L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
def print_list(lst):
    for x in lst:
        # 如果x绑定数字,打印数字
        if type(x) is int:
            print(x)
        # 如果x绑定列表,打印列表
        elif type(x) is list:
            print_list(x)

print_list(L)


def sum_list(lst):
    s = 0
    for x in lst:
        # 如果x是数字,则把x加到s中
        if type(x) is int:
            s += x
        # 如果x是列表,把列表的和加到s中
        else:
            s += sum_list(x)
    return s

print(sum_list(L))  # 106
