#   输入三行文字,让这三行文字依次以 20个字符的宽度右对齐
#   输出
#     如:
#       请输入第1行: hello world!
#       请输入第2行: abcd
#       请输入第3行: a
#     输出结果为:
#                hello world!
#                        abcd
#                           a
#   做完上面的题后再思考:
#     能否以最长字符串的长度进行右对齐显示(左侧填充空格)

s1 = input("请输入第1行: ")
s2 = input("请输入第2行: ")
s3 = input("请输入第3行: ")
# 方法1
# zuida = len(s1)
# if len(s2) > zuida:
#     zuida = len(s2)
# if len(s3) > zuida:
#     zuida = len(s3)
# 方法2
zuida = max(len(s1), len(s2), len(s3))
print("最长的字符串长度是:", zuida)

# 右对齐方法1
# print(' ' * (zuida-len(s1)) + s1)
# print(' ' * (zuida-len(s2)) + s2)
# print(' ' * (zuida-len(s3)) + s3)

# 右对齐方法2
fmt = "%" + str(zuida) + "s"

print(fmt % s1)
print(fmt % s2)
print(fmt % s3)
