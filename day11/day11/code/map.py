# map.py

def power2(x):
    print("++++++++++++++++")
    return x ** 2

# 生成一个可迭代对象,此可迭代对象可以生成1~9的自然数的平方
# 1 4 9 16 .....
for x in map(power2, range(1, 10)):
    print(x)

