#   2. 输入一个学生的三科成绩:
#         打印出最高分是多少?
#         打印出最低分是多少?
#         打印出平均分是多少?

a = int(input("请输入第1科成绩: "))
b = int(input("请输入第2科成绩: "))
c = int(input("请输入第3科成绩: "))

zhuida = a
if b > zhuida:
    zhuida = b

if c > zhuida:
    zhuida = c

print('最大数是:', zhuida)






