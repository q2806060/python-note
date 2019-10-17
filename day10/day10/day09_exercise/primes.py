#   1. 素数练习:
#     1) 写一个函数isprime(x)  判断x是否为素数,如果是素数
#        返回True,否则返回False
#        如:
#         print(isprime(3))  # True
#         print(isprime(4))  # False
#     2) 写一个函数prime_m2n(m, n)  返回从m开始,到n结束
#        范围内的素数,返回这些素数的列表,并打印(注:不包含n)
#        如:
#         L = prime_m2n(10, 20)
#         print(L)  # [11, 13, 17, 19]
#     3) 写一个函数 primes(n) 返回指定范围内的全部素数(不包
#        含n)的列表
#        如:
#        L = primes(10)
#        print(L)  # [2, 3, 5, 7]
#        1> 计算100以内的全部素数的和
#        2> 计算100~200之间全部素数的和



# 1) 写一个函数isprime(x)  判断x是否为素数,如果是素数
#     返回True,否则返回False
#     如:

def isprime(x):
    if x < 2:
        return False
    # 直到此数x一定大于等于2, 用排除法,一旦x能被 2~x-1的
    # 整数整除,一定不是素数
    for i in range(2, x):  # i绑定是的整数
        if x % i == 0:
            return False
    # 走到此处x一定是素数
    return True


print(isprime(3))  # True
print(isprime(4))  # False
# 2) 写一个函数prime_m2n(m, n)  返回从m开始,到n结束
#     范围内的素数,返回这些素数的列表,并打印(注:不包含n)
#     如:
def prime_m2n(m, n):
    # 方法1
    # L = []
    # for x in range(m, n):
    #     if isprime(x):
    #         L.append(x)
    # return L
    # 方法2 用列表推导式
    return [x for x in range(m, n) if isprime(x)]

L = prime_m2n(10, 20)
print(L)  # [11, 13, 17, 19]

# 3) 写一个函数 primes(n) 返回指定范围内的全部素数(不包
#     含n)的列表
#     如:
def primes(n):
    return prime_m2n(0, n)

L = primes(10)
print(L)  # [2, 3, 5, 7]
# 1> 计算100以内的全部素数的和
print("100以内的全部素数的和=", sum(primes(100)))
# 2> 计算100~200之间全部素数的和
print("100~200之间全部素数的和", sum(prime_m2n(100, 200)))

