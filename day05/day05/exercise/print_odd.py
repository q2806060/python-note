#   1. 打印 100 以内的奇数,打印在一行内
#      可以采用跳过偶数的方式


for x in range(0, 100):
    if x % 2 == 0:
        continue
    print(x, end=' ')
print()

