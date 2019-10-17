# recursion_myfac.py

# 此示例示意用递归的方式求阶乘
def factorial(n):
    # print("n=", n)
    # 如果n为0,则0! = 1
    if n == 0:
        return 1
    # 如果n 不为0, n! = n * (n-1)!
    r = n * factorial(n -1)
    return r

print(factorial(5))  # 120