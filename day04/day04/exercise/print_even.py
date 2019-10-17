# 练习:
#   输入任意一个数n,此数代表结束的数(不包含n)
#     打印 从 0开始 至 n的偶数
#       0 2 4 6 8 ..... n-1/n-2
#     打印在一行内

n = int(input("请输入一个结束整数n: "))

# 方法1
i = 0
while i < n:
    if i % 2 == 0:
        print(i, end=' ')
    i += 1
else:
    print()  # 换行

# 方法2
i = 0
while i < n:
    print(i, end=' ')
    i += 2
else:
    print()