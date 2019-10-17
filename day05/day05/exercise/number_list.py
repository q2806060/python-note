#   1. 写一个程序,让用户输入很多个正整数,当输入负数时结束
#      输入,将用户输入的数字存于列表L 中
#        1) 打印这个列表
#        2) 打印这个列表中所有元素的和
#        3) 打印这个列表中所有元素的平方和
#      如:
#        输入: 1
#        输入: 2
#        输入: 3
#        输入: -1
#      结果:
#        列表是:[1, 2, 3]
#        和是: 6
#        平方和是: 14

L = []  # 先创建一个列表,准备向其中添加数据
while True:
    n = int(input("请输入正整数: "))
    if n < 0:
        break
    L += [n]

print("列表是:", L)

# 打印所有元素的和
s = 0
for x in L:
    s += x
print("和是:", s)

# 打印所有元素的平方和
s2 = 0
for x in L:
    s2 += x ** 2
print("平方和是:", s2)

