# while_embed.py
# 打印 1 ~ 20 的整数,打印在一行内
# 打印 10 行

j = 0
while j < 10:
    # print('1 2 3 4 5 6 .... 19 20')
    i = 1
    while i <= 20:
        print(i, end=' ')
        if i == 15:
            break
        i += 1

    print()

    j += 1

print("程序结束")

    