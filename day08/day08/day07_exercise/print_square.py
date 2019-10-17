#   2. 输入一个数,代表图形的宽度, 打印如下正方形
#     如:
#       输入: 5
#     打印:
#       1 2 3 4 5
#       2 3 4 5 6
#       3 4 5 6 7
#       4 5 6 7 8
#       5 6 7 8 9
#     如:
#       输入: 3
#     打印:
#       1 2 3
#       2 3 4
#       3 4 5

n = int(input("请输入宽度: "))

for line in range(1, n + 1):  # line代表的是当前行号
    # 从line开始，向后打印n个数字，每个数字加1
    for x in range(line, line + n):
        # print(x, end=' ')
        print("%02d" % x, end=' ')
    print()  # 换行

