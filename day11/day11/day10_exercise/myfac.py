#   2. 写一个函数myfac(n)  来计算n!(n的阶乘)
#     n! = 1 * 2 * 3 * 4 * ... * n
#   如:
#     print(myfac(5))   # 120

def myfac(n):
    s = 1
    for x in range(1, n + 1):
        s *= x
    return s

print(myfac(5))
