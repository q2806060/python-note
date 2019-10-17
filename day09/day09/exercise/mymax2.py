# 练习:
#   已知内建函数max帮助方档为:
#     max(iterable)
#     max(arg1, arg2, *args)
#   仿造max, 写一个mymax函数,功能与max完全相同
#   (要求不允许调用max函数)
#     print(mymax([6, 8, 3, 5]))  # 8
#     print(mymax(100, 200))  # 200
#     print(mymax(1, 3, 9, 5, 7))  # 9


def mymax(*args):
    # print('args=', args)
    # 当元组长度为1时,传入的是一个列表
    if len(args) == 1:
        iterable = args[0]
        zd = iterable[0]
        for x in iterable:
            if x > zd:
                zd = x
        return zd
    else:
        zd = args[0]
        for x in args:
            if x > zd:
                zd = x
        return zd


print(mymax([6, 8, 3, 5]))  # 8
print(mymax(100, 200))  # 200
print(mymax(1, 3, 9, 5, 7))  # 9

print(max([6, 8, 3, 5]))  # 8
print(max(100, 200))  # 200
print(max(1, 3, 9, 5, 7))  # 9


