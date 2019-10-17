# filter.py

# 把一个可迭代对象中的所有奇数放在一个列表内
L = [1, 2, 6, 8, 5, 4, 2, 1, 3, 6, 8, 9]

def isodd(x):
    '''如果x为奇数返回True,否则返回False'''
    return x % 2 == 1

L2 = []
for x in filter(isodd, L):
    # print(x)
    L2.append(x)
print("L2=", L2)

L3 = [x for x in filter(isodd, L)]
print("L3=", L3)

L4 = list(filter(isodd, L))
print("L4=", L4)

