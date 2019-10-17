# break.py

i = 1
while i <= 6:
    print("循环开始: ", i)
    if i == 3:
        break

    print("循环结束:", i)
    i += 1
else:
    print("while里的else子句被执行!")

print("程序结束")
