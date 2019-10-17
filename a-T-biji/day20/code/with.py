# with.py


# 此示例示意用with语句和try-finally 来保证文件的正确关闭

fr = open("../day20.txt")  # 打开文件
try:
    s = fr.read()  # 读取文件
    print("字符个数是:", len(s))
finally:
    fr.close()  # 关闭文件

