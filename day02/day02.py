#! /usr/bin/python3


# num = float(input())
# if num >= 0:
#     print(num)
# else:
#     print(-num)


# num = float(input())
# num = num if num > 0 else -num
# print(num)


# score = float(input('请输入成绩：'))
# if 0 <= score <= 100:
#     pass
# else:
#     print('成绩不合法.')

x = float(input('请输入行驶公里数：'))
if 0 < x <= 3:
    print('您需支付１３元.')
elif 3 < x <= 15:
    price = 13 + 2.3 * (x-3)
    print('您需支付',round(price),'元.')
elif x > 15:
    price = 13 + 3.4 * (x - 15) + 2.3 * (15 - 3)
    print('您需支付',round(price),'元.')

a = float(input('请输入语文成绩：'))
b = float(input('请输入数学成绩：'))
c = float(input('请输入英语成绩：'))

zuida = a
if b > zuida:
	zuida = b
if c > zuida:
	zuida = c
print('最大值是:',zuida)

zuixiao = a 
if zuixiao > b:
	zuixiao = b
if zuixiao > c:
	zuixiao = c
print('最小值是:',zuixiao)



year = int(input('请给出一个年份：'))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('该年份是闰年.')
else:
    print('该年份不是闰年.')


heigh = float(input('请输入您的身高（公分）：'))
weight = float(input('请输入您的体重（公斤）：'))
BMI = weight / (heigh / 100) ** 2
if BMI < 18.5:
    print('您的体重过轻.')
elif 18.5 <= BMI <= 24:
    print('您的体重正常.')
else:
    print('您的体重过重.')





































