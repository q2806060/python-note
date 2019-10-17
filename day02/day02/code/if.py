# if.py


# 此示例示意if语句的基本语句和用法
# 让用户输入一个整数,判断这个整数是奇数还是偶数

num = int(input("请输入一个整数: "))
if num % 2 == 1:  # 余1为奇数
    print(num, '是奇数')
elif num % 2 == 0:
    print(num, '是偶数')
