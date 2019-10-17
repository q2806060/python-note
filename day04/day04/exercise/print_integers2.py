#   2. 写一个程序
#     输入一个开始的整数 用变量begin绑定
#     输入一个结束的整数用变量end绑定
#     打印 从 begin 到 end(不包含end) 的每个整数,在印在
#     一行内
#       如:
#         请输入开始值: 8
#         请输入结束值: 20
#       打印:
#         8 9 10 11 12 13 .... 19

#     思考,如何实现每5个数字打印在一行内,打印多行
#       提示: 多加一个变量来记录打印的个数

begin = int(input("请输入开始值: "))
end = int(input("请输入结束值: "))

count = 0   # 变量用来记录已打印的次数

while begin < end:
    print(begin, end=' ')
    count += 1  # 记录次数
    if count % 5 == 0:
        print()  # 换行
    # 当上述循环完成时
    begin += 1

print()  # 换行