#   2. 写一个函数print_even,传入一个参数n代表终止整数
#     此函数打印 2 4 6 .... n(不包含n)以内的所有偶数
#     函数定义如下:
#       def print_even(n):
#           ..... # 此处自己实现
      
#       print_even(10)
#       打印
#       2
#       4
#       6
#       8


def print_even(n):
    for x in range(2, n, 2):
        print(x)

print_even(10)
# 打印
# 2
# 4
# 6
# 8