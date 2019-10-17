#   3. 输入三行文字,让这三行文字在一个方框内居中显示
#     如输入(不要输入中文):
#       hello!
#       I'm studing python!
#       I like python!
#     显示如下:
#       +---------------------+
#       |        hello!       |
#       | I'm studing python! |
#       |   I like python!    |
#       +---------------------+

s1 = input("请输入第1行: ")
s2 = input("请输入第2行: ")
s3 = input("请输入第3行: ")
max_length = max(len(s1), len(s2), len(s3))

first_line = '+-' + '-' * max_length + '-+'
print(first_line)

# 打印第 2, 3, 4行
print('| ' + s1.center(max_length) + ' |')
print('| ' + s2.center(max_length) + ' |')
print('| ' + s3.center(max_length) + ' |')

# 打印最后一行
print(first_line)

