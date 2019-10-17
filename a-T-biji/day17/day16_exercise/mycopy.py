#! /usr/bin/python3

#   1. 写程序,实现复制文件的功能
#     要求:
#       1) 要考虑文件关闭的问题
#       2) 要考虑超大文件的问题(文件太大时将无法全部加载到内存)
#       3) 要能复制二进制文件

import sys
# print(sys.argv)
if len(sys.argv) < 3:
    print('''用法:  ./mycopy 源文件路径名 目标文件路径名''')
    sys.exit()

src_file = sys.argv[1]  # 源文件名
dst_file = sys.argv[2]  # 目标文件名

def copy_file(src, dst):
    print("正在从", src, '复制到', dst)
    try:
        fr = open(src, 'rb')
        try:
            fw = open(dst, 'wb')
            try:
                while True:
                    b = fr.read(4096)  # 每次搬运4096
                    if not b:  # 当字节串为空,此时复制完毕
                        break
                    fw.write(b)
            finally:
                fw.close()
        finally:
            fr.close()
        print("复制成功")
    except OSError:
        print('复制失败!')
copy_file(src_file, dst_file)

