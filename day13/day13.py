#1

# import math

# r = float(input('半径：'))
# s = math.pi * r ** 2
# print('面积：', s)

# s = float(input('面积：'))
# r = math.sqrt(s / math.pi)
# print('半径：', r)


# 练习

import time

y = int(input('请输入你的出生年份：'))
m = int(input('请输入你的出生月份：'))
d = int(input('请输入你的出生日期：'))
birth_tuple = (y, m, d, 0, 0, 0, 0, 0, 0)
birth_second = time.mktime(birth_tuple)
cur_second = time.time()
life_second = cur_second - birth_second
life_days = life_second / 3600 // 24
print('您已出生：', life_days, '天')


t = time.localtime(birth_second)
weeks = {
    0:'星期一',
    1:'星期二',
    2:'星期三',
    3:'星期四',
    4:'星期五',
    5:'星期六',
    6:'星期日',
}

print('您出生那天是：', weeks[t[5]])







































































































