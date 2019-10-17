# 3. 写一个函数mypow(n)计算
#  1 + 2**2 + 3**3 + ... n**n的和
#     (注: n给个小点的数)
#    如:
#     print(mypow(3))  # 32

def mypow(n):
    # 方法1
    # s = 0
    # for x in range(1, n + 1):
    #     s += x ** x
    # return s

    # 方法2
    return sum(map(lambda x:x**x, range(1, n+1)))

print(mypow(3))  # 32
