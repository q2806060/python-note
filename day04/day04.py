#! /usr/bin/python3

#1

# print('I\'m a teacher')

#2

# a = int(input('请输入一个数字：'))
# print('#' * a)
# print('#' + (' ' * (a-2)) + '#')
# print('#' + (' ' * (a-2)) + '#')
# print('#' * a)

#3

# x = input('请输入一串字符：')
# print(x[0])
# print(x[-1])
# if len(x) % 2 == 1:
#     print(x[(len(x) - 1) // 2])

#4

# x = input('请输入一串字符：')
# a = x[1:(-1)]
# print(a)

# x = input('请输入一串字符：')
# b = x[::(-1)]
# if x == b:
#     print('该字符串为回文.')

#5

# s = 'ABCD1234'
# print(max(s))
# print(min(s))

#6

# print(ord('许'))
# print(ord('道'))
# print(ord('林'))
# print(chr(26519))

#7

# x = input('请输入一串字符：')
# if len(x) != 0:
#     print(ord(x[0]))

# x = int(input('请输入整数值：'))
# print(chr(x))

#8  练习

a = int(input('请输入一个整数：'))
b = '   *   '
c = '  ***  '
d = ' ***** '
e = '*******'
print(' ' * a + b)
print(' ' * a + c)
print(' ' * a + d)
print(' ' * a + e)


b = input('请输入一个字符串：')
c = b.replace(' ','')
print(c)


d = input('请输入一串文字：')
e = input('请输入一串文字：')
f = input('请输入一串文字：')
x = len(d)
y = len(e)
z = len(f)
long = x
if long < y:
    long = y
if long < z:
    long = z
print('+' + '-' * long + '+')
print('|' + d.center(long) + '|')
print('|' + e.center(long) + '|')
print('|' + f.center(long) + '|')
print('+' + '-' * long + '+')









