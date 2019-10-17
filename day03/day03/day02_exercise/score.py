#   2. 输入一个学生的三科成绩:
#         打印出最高分是多少?
#         打印出最低分是多少?
#         打印出平均分是多少?

a = int(input("请输入第1科成绩: "))
b = int(input("请输入第2科成绩: "))
c = int(input("请输入第3科成绩: "))

if a > b:
    # a大
    if a > c:
        print("最大值是:", a)
    else:
        print("最大值是:", c)
else:
    # b大
    if b > c:
        print("最大值是:", b)
    else:
        print("最大值是:", c)




