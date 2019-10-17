#    2. 计算出100以内的全部素数，将这些素数存于列表中.
#      最后打印出这些素数

L = []  # 此列表用来存入素数

for x in range(2, 101):
    # 判断如果x是素数,就把x放入列表L中
    for i in range(2, x):
        if x % i == 0:  # x不是素数
            break
    else:  # 如没有break退出此循环.x一定是素数
        L.append(x)

print("L=", L)