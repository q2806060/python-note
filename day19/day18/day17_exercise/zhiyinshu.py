#   1. 分解质因数,输入正整数,分解质因数:
#     如
#       输入:
#         90
#     打印如下:
#       90=2*3*3*5
#     质因数是指最小能被原数整数的素数(不包括1)

def get_yinshu_list(n):
    '''此函数用于获取n的所有因数的列表'''
    L = []  # 用于保存列表
    # 在此处算出n的质因数
    while n != 1:
        # 每次循环得到一个质因数放入L中,
        for i in range(2, n + 1):
            if n % i == 0:  # i为n的质因数
                L.append(i)  # 保存此质因数
                # 再修改n的值为 n = int(n /  当前质因数)
                n = int(n // i)
                break  # 只要找到一个就结束当前循环

    return L

def get_yinshu_str(L):
    L2 = [str(x) for x in L]
    return '*'.join(L2)

n = int(input("请输入一个大于1的整数: "))
L = get_yinshu_list(n)
s = get_yinshu_str(L)
print(n, '=', s)

