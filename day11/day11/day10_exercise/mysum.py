#   1. 写一个函数mysum(x)  来计算:
#     1 + 2 + 3 + 4 + ..... + n 的值
#     (要求: 不允许用sum)
#   如:
#     print(mysum(100))  # 5050


def mysum(n):
    '''此函数的目的是返回
    1 + 2 + 3 + 4 + ..... + n 的值
    '''
    s = 0
    for x in range(1, n + 1):
        s += x
    return s


print(mysum(100))  # 5050
