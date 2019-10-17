#   1. 用字符串 * 星号打印圣诞树
#     输入一个整数,代表树干的高度
#     如: 
#       输入: 2
#     打印:
#        *
#       ***
#        *
#        *
#     如: 
#       输入: 3
#     打印:
#         *
#        ***
#       *****
#         *
#         *
#         *

n = int(input("请输入树干的高度: "))

width = n * 2 - 1  # 先算出最下一层的树叶的宽度
for line in range(1, n + 1):  # line 代表行数
    star = line * 2 - 1 # 星号个数
    s = '*' * star  # 得到星号字符串
    print(s.center(width))  # 居中打印

# 打印树干
for _ in range(n):
    print("*".center(width))


