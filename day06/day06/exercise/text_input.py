# 练习:
#   输入多行文字,存入列表中
#     每次输入后回车算作一行
#     任意输入多行,当直接输入回车键(即空行) 结束输入
#   要求:
#     1. 按原输入的顺序把输入内容在终端上显示
#     2. 打印出您共输入了多少行文字
#     3. 打印您共输入了多少个字符

L = []  # 创建一个列表,用来存字符串
while True:
    s = input("请输入: ")
    if s == '':  # 或 if not s:
        break
    L.append(s)  # 把s绑定的字符串放在L内

# print("L=", L)
print("----------------原内容如下:-----------")
for text in L:
    print(text)
print("----------------end-----------------")
print("您共输入了%d行" % len(L))
count = 0  # 用来累加字符个数
for text in L:
    count += len(text)
print("您共输入了%d个字符" % count)




