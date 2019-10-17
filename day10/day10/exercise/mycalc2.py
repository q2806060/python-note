# 练习:
#     写一个计算公式的解释执行器
#       已知有如下一些函数:
#         def myadd(x, y):
#             return x + y
#         def mysub(x, y):
#             return x - y
#         def mymul(x, y):
#             return x * y
#         ...
#       再写一个函数
#         def get_func(op):
#             .....  # 以下代码自己实现
#         此函数在传入字符串"加"或'+' 返回myadd函数
#         此函数在传入字符串"乘"或'*'  返回mymul函数
#       在主函数程序如下:
#         def main():
#             while True:
#                 s = input("请输入计算公式: ")  # 10 加 20
#                 L = s.split()  # L = ['10', '加', '20']
#                 a = int(L[0])
#                 b = int(L[2])
#                 fn = get_func(L[1])
#                 print("结果是:", fn(a, b))  # 结果是: 30
#         main()




def get_func(op):
    def myadd(x, y):
        return x + y

    def mysub(x, y):
        return x - y

    def mymul(x, y):
        return x * y

    if op == '+' or op == '加':
        return myadd
    elif op in ('-', '减'):
        return mysub
    elif op in ('*', '乘'):
        return mymul

def main():
    while True:
        s = input("请输入计算公式: ")  # 10 加 20
        L = s.split()  # L = ['10', '加', '20']
        a = int(L[0])
        b = int(L[2])
        fn = get_func(L[1])
        print("结果是:", fn(a, b))  # 结果是: 30

main()
