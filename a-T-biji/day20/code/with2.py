# with2.py


# 此示例示意用with语句和try-finally 来保证文件的正确关闭

# fr = open("../day20.txt")  # 打开文件
try:
    with open("../day20.txt") as fr:
        s = fr.read()  # 读取文件
        100 / 0
        print("字符个数是:", len(s))
except ZeroDivisionError:
    print('发生被零除的错误!')

# fr.read() # 错的 此时文件已经在结束with语句时被关闭
print("程序结束")