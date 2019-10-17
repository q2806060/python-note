#   2. 分三次输入当前的小时,分钟, 秒数
#       在终端打印距离凌晨0:0:0过了多少秒?

hour = int(input("请输入小时: "))
minute = int(input("请输入分钟: "))
second = int(input("请输入秒: "))

s = hour * 60 * 60 + minute * 60 + second
print("距离0:0:0过了", s, '秒!')
