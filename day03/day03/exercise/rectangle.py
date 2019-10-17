# 练习:
#   写一个程序,打印一个高度为4行的矩形方框
#     要求输入一个整数,此整数代表矩形的宽度,输出此矩形:
#   如:
#     请输入矩形的宽度: 10
#   打印如下:
#     ##########
#     #        #
#     #        #
#     ##########

width = int(input("请输入矩形宽度: "))
line1 = "#" * width
print(line1)

if width == 1:
    line2 = '#'
else:
    line2 = '#' + ' ' * (width - 2) + '#'

print(line2)
print(line2)
print(line1)



