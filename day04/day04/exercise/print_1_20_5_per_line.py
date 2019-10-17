#   3. 打印1 ~ 20的整数,每行打印5个,打印4行
#      1 2 3 4 5
#      6 7 8 9 10
#      11 12 ...
#      ....

i = 1
while i <= 20:
    print(i, end=' ')
    if i % 5 == 0:
        print()  # 换行
    # if i == 5:
    #     print()  # 换行
    # elif i == 10:
    #     print()
    # elif i == 15:
    #     print()
    # elif i == 20:
    #     print()
    i += 1

    