# sys_exit.py


def f1():
    print('aaaaa')
    # 能否在此处不返回到调用的方就退出程序呢?
    import sys
    sys.exit()

    print('bbbbb')

f1()
print('程序结束')