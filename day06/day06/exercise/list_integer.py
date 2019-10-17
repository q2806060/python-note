#   2. 写程序,让用户输入很多个整数(包含正整数和负整数) 保存在
#     列表L 中,输入0时结束输入,
#       1. 把列表L中所有的正整数存于L2列表中
#       2. 把列表L中所有的负整数存于L3列表中
#     打印原列表L, 正整数列表L2 和 负整数列表 L3

L = []
while True:
    n = int(input("请输入整数: "))
    if n == 0:
        break
    L.append(n)

L2 = [x for x in L if x > 0]  # 选出正整数
L3 = [x for x in L if x < 0]  # 这出负整数

print("原数据是:", L)
print("正整数是:", L2)
print("负整数是:", L3)

