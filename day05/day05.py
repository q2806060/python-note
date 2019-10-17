#! /usr/bin/python3

#1

# fmt = '姓名：%s, 年龄：%d'
# print(fmt %('tarena', 15))

#2

# a = input('请输入一行文字：')
# b = input('请输入一行文字：')
# c = input('请输入一行文字：')

# long_str = max(len(a),len(b),len(c))

# str_in = '%' + str(long_str) + 's'

# print(str_in %a)
# print(str_in %b)
# print(str_in %c)

#3

# a = int(input('输入一个整数：'))

# for i in range(1 , a + 1):
#     print('这是第%d行.' %i)

# b = 1
# while b <= a:
#     print('这是第%d行.' %b)
#     b += 1

#4

# i = 1
# while i <= 20:
#     print(i)
#     i += 1

# i = 1
# while i <= 20:
#     print(i, end = ' ')
#     i += 1
# else:
#     print()

# i = 1
# while i <= 20:
#     print(i, end = ' ')
#     if i % 5 == 0:
#         print()
#     i += 1
    
#5

# a = int(input('输入一个整数：'))

# i = 0 
# while i < a:
#     if i % 2 == 0:
#         print(i,end = ' ')
#     i += 1
# else:
#     print()
        
#6

# begin = int(input('输入一个整数：'))
# end = int(input('输入一个整数：'))
# step = begin
# while begin < end:
#     if (begin - step) % 5 ==0 and begin - step != 0:
#         print()
#     print(begin, end = ' ')
#     begin += 1
# print()

#7

# begin = int(input('输入一个整数：'))
# end = int(input('输入一个整数：'))
# i = 0
# while begin <= end:
#     i += begin
#     print(i)
#     begin += 1
# print(i)

#8

# a = int(input('输入一个整数：'))
# b = 0
# while b < a:
#     c = 1
#     while c <= a:
#         print(c, end = ' ')
#         c += 1
#     else:
#         print()
#     b += 1

#9

# b = 0
# while True:
#     a = int(input('输入一个整数：'))
#     if a < 0:
#         print(b)
#         break
#     b += a

#10

# a = int(input('输入一个整数：'))
# b = 0
# if a == 1:
#     print('#')
# else:
#     print('#' * a)
#     while b < (a - 2):
#         print('#' + ' ' * (a-2) + '#')
#         b += 1
#     print('#' * a)
        
# 练习

# a = 65
# s = ''
# while a <= 90:
#     s += chr(a)
#     a += 1
# print(s)


# a = 65
# b = 97
# s = ''
# while a <= 89:
#     s += chr(a)
#     s += chr(b)
#     a += 1
#     b += 1
# print(s)


# a = int(input('输入一个整数：'))
# b = 1
# while b <= a:
#     print('*' * b)
#     b += 1

# c = 1
# while c <= a:
#     print(' ' * (a - c) + '*' * c)
#     c += 1

# d = 0
# while d < a:
#     print('*' * (a - d) + ' ' * (d))
#     d += 1

# e = 0
# while e < a:
#     print(' ' * e + '*' * (a - e))
#     e += 1



begin = int(input('请输入起始值：'))
end = int(input('请输入终止值：'))
while begin <= end:
    print(begin, hex(begin), chr(begin))
    begin += 1













































































