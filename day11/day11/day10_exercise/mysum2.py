#   1. 写一个函数mysum(x)  来计算:
#     1 + 2 + 3 + 4 + ..... + n 的值
#     (要求: 不允许用sum)
#   如:
#     print(mysum(100))  # 5050


def mysum(n):
    return sum(range(1, n + 1))



print(mysum(100))  # 5050
