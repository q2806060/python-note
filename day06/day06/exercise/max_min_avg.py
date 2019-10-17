# 练习:
#   1. 输入三个数存于列表中,打印出这三个数的最大值,最小值
#     和平均值.

n1 = int(input("请输入第1个数: "))
n2 = int(input("请输入第2个数: "))
n3 = int(input("请输入第3个数: "))

L = [n1, n2, n3]
zd = max(L)  # 求最大值
zx = min(L)
avg = sum(L)/len(L)
print("最大值是:", zd)
print("最小值是:", zx)
print("平均值是:", avg)

