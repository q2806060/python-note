#1

# import random
# x = random.randint(0, 100)
# while True:
#     y = int(input('请输入一个整数(0-100):'))
#     if y > x:
#         print('您猜大了！')
#     if y < x:
#         print('您猜小了！')
#     if y == x:
#         print('您猜对了！')
#         break
    

# 练习

import random
# t = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
#      'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
#      's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


# l = [chr(x) for x in range(97, 97 + 26)]
# l += [chr(x) for x in range(65, 65 + 26)]
# l += [chr(x) for x in range(ord('0'), ord('0') + 10)]
# t = l
# s = ''
# for i in range(6):
#     s0 = str(random.choice(t))
#     s += s0
# print(s)





import random

flowwers = ('\u2660', '\u2663', '\u2666', '\u2665')
card_face = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
king = ['kb', 'ks']
l = []
for x in flowwers:
    for y in card_face:
        if x + y not in l:
                l.append(x + y)
l.extend(king)
l1 = random.sample(l, 17)
for i in l1:
    l.remove(i)
l2 = random.sample(l, 17)
for i in l2:
    l.remove(i)
l3 = random.sample(l, 17)
for i in l3:
    l.remove(i)
input()
print(l1)
input()   
print(l2)
input()
print(l3)
input()
print(l)




































































































