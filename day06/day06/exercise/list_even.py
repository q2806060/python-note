#  1. 输入一个开始的整数用begin绑定
#     输入一个结束的整数用end绑定
#     将从begin开始,到end结束的所有偶数存于列表中,并打印这
#     个列表
#     (建议用列表推导式实现) 

begin = int(input('请输入开始整数: '))
end = int(input("请输入结束整数: "))
L = [x for x in range(begin, end) if x % 2 == 0]
print(L)
