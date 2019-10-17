# if_elif_else.py


# 输入一个数字,用程序来判断这个数是正数,负数还是零
num = int(input("请输入整数: "))
if num > 0:
    print(num, '是正数')
elif num < 0:
    print(num, '是负数')
else:
    print(num, '是零')