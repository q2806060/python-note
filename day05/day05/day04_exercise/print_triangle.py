#   2.  用while语句实现打印三角形,输入一个整数n表示三角形
#     直角边的宽度和高度,打印相应的三角形
#     如:
#       请输入三角形的宽度: 4
#     第一种打印:
#       *
#       **
#       ***
#       ****
#     第二种打印:
#          *
#         **
#        ***
#       ****
#     第三种打印:
#       ****
#        ***
#         **
#          *
#     第四种打印:
#       ****
#       ***
#       **
#       *



w = int(input("请输入三角形的宽度: "))
line = 1  # 代表行
while line <= w:
    # 打印一行
    print("*" * line)
    line += 1

print('-----------------------------')
line = 1
while line <= w:
    blank = w - line  # 计算空格的个数
    print(' ' * blank + '*' * line)
    line += 1

print('-----------------------------')
star = w  # 代表星的个数
while star > 0:
    blank = w - star   # 计算空格的个数
    print(' ' * blank + '*' * star)
    star -= 1

print('-----------------------------')
star = w  # 代表星的个数
while star > 0:
    print('*' * star)
    star -= 1
# 第四种打印:
#   ****
#   ***
#   **
#   *
