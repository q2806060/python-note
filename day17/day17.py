
#1

# try:
#     fr = open('day17/day17.txt', encoding = 'utf-8')
#     s = fr.read()
#     print(s)
#     print(len(s))
#     fr.close()
# except OSError:
#     print('文件打开失败！')


#2

# try:
#     fr = open('day17/info.txt', encoding = 'utf-8')
#     while True:
#         s = fr.readline()
#         if s == '':
#             break
#         s1 = s.split()
#         print(s1[0] + '今年' + s1[1] + '岁，成绩是：' + s1[2])
#     fr.close()
# except OSError:
#     print('文件打开失败！')


#3

# try:
#     fw = open('day17/my_bin_file.txt', 'wb')
#     b = bytes(range(256))
#     fw.write(b)
#     fw.close()
# except OSError:
#     print('文件打开失败！')


#4


# def input_info():
#     l = []
#     while True:
#         name = input('请输入姓名：')
#         if not name:
#             break
#         num = input('请输入电话号码：')
#         t = (name, num)
#         l.append(t)
#     return l 

# def write_to_file(l):
#     try:
#         f = open('day17/phone_num.txt', 'w')
#         for name, num in l:
#             f.write(name)
#             f.write(',')
#             f.write(num)
#             f.write('\n')       
#         f.close()
#     except OSError:
#         print('写文件失败！')

# l = input_info()
# write_to_file(l)


# 练习


import sys
# print(sys.argv)

src_file = sys.argv[1]
dst_file = sys.argv[2]

def copy_file(src, dst):
    fr = open(src, 'rb')
    fw = open(dst, 'wb')
    while True:
        b = fr.read(4096)
        if not b:
            break
        fw.write(b)

    fr.close()
    fw.close()

copy_file(src_file, dst_file)































































