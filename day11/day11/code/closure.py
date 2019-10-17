# closure.py

# 定义一些函数,让这些函数能实现求x的n次方
# 示意
# def pow2(x):
#     return x ** 2

# def pow3(x):
#     return x ** 3
# ...
# def pow100(x):
#     return x ** 100


def make_power(y):
    def fn(x):
        return x ** y
    return fn

pow3 = make_power(3)
pow2 = make_power(2)
pow100 = make_power(100)


print("5的立方是:", pow3(5))
print("6的平方是:", pow2(6))
print("2的100次方是:", pow100(2))
