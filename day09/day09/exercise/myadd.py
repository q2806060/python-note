# 练习:
#   写一个函数myadd, 此函数可以计算两个数,三个数,及四个数的和
#     def myadd(.....):
#        ....

#     print(myadd(10, 20))  # 30
#     print(myadd(100, 200, 300))  # 600
#     print(myadd(1, 2, 3, 4))  # 10

# 方法1
# def myadd(a, b, c=0, d=0):
#     return a + b + c + d

# 方法2
# def myadd(a, b, c=None, d=None):
#     if c is None:
#         c = 0
#     if d is None:
#         d = 0
#     return a + b + c + d

# 方法3
def myadd(a, b, c=0, d=0):
    return sum( (a, b, c, d) )

print(myadd(10, 20))  # 30
print(myadd(100, 200, 300))  # 600
print(myadd(1, 2, 3, 4))  # 10


