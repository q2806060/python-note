#   2. 写程序,让用户循环输入一些整数,当输入-1时结束输入,
#   将这些整数存于列表L中
#      1) 打印您共输入了几个有效的数(不包含结束时输入的负数)
#      2) 打印您输入的数的最大数是多少?

#     试想不用max,min, sum等函数能否实现上述功能?

L = []  # 先创建容器
while True:
    n = int(input("请输入整数: "))
    # if n < 0:
    if n == -1:
        break
    L += [n]  # 追加  # L[0:0] = [n]  头插

print("L=", L)
print("您输入的有效的数是:", len(L))
print('您输入最大数是:', max(L))

print("------以不用内建函数最有效个数和最大数-----")
count = 0
for _ in L:
    count += 1

print("有效数是:", count)
# 以下求最大:
zd = L[0]
for x in L:
    if x > zd:
        zd = x
print("最大数是:", zd)
