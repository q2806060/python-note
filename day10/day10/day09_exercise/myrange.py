#   2.  写一个myrange函数,参数可以传1~3个,实际含义与range函数相同
#      此函数返回符合range() 函数规则的列表:
#        如:
#         L = myrange(4)
#         print(L)  # [0, 1, 2, 3]
#         L = myrange(4, 6)
#         print(L)  # [4, 5]
#         L = myrange(1, 10, 3)
#         print(L)  # [1, 4, 7]
#         L = myrange(10, 0, -3)
#         print(L)  # [10, 7, 4, 1]

def myrange(start, stop=None, step=None):
    if stop is None:  # 校正开始和结束值
        stop = start
        start = 0
    if step is None:
        step = 1
    if step > 0:  # 正向
        L = []
        while start < stop:
            L.append(start)
            start += step
        return L
    else:  # 反向
        L = []
        while start > stop:
            L.append(start)
            start += step  # 注意此时step为负数
        return L
L = myrange(4)
print(L)  # [0, 1, 2, 3]
L = myrange(4, 6)
print(L)  # [4, 5]
L = myrange(1, 10, 3)
print(L)  # [1, 4, 7]
L = myrange(10, 0, -3)
print(L)  # [10, 7, 4, 1]
