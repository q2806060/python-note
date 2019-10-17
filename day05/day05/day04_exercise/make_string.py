#   1. 用程序while 语句生成如下字符串:
#         字符串1:  'ABCDEFG.......XYZ'
#         字符串2:  'AaBbCcDdEeFfGg......XxYyZz'
#     提示:
#         s = ''
#         s += 'A'  # s += chr(65)
#         s += 'a'  # s += chr(97)

# 生成 'ABCDEFG.......XYZ'

start = ord('A')  # 第一个A的值
end = ord('Z')  # 最后一个元素的值
s = ''  # 空字符串用于累加
while start <= end:
    s += chr(start)
    start += 1
print("第一个字符串是:", s)

start = ord('A')
end = ord('Z')
s = ''
while start <= end:
    # 1. 追加一个大写的字符
    s += chr(start)
    # 2. 追加一个小写的字符
    s += chr(start + 32)  # 32来自于ord('a')-ord('A')
    start += 1
print("第二个字符串是:", s)



