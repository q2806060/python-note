#1


# import random

# def value(values=[]):
#     while len(values) <= 20:
#         x = random.randint(1, 21)
#         if x not in values:
#             values.append(x)
#         else:
#             continue
#     print(values)
#     return values
    
# def linear(values, key):
#     for i in range(len(values)):
#         if values[i] == key:
#             return i

# key = 6
# res = linear(value(), key)
# if res == -1:
#     print('查找失败！')
# else:
#     print('查找成功！')




#2


# values = sorted([18, 8, 3, 14, 15, 10, 7, 19, 21, 4, 1, 20, 6, 16, 13, 11, 2, 17, 12, 5, 9])

# def search_num(values, key, count=0):
#     if values[len(values)//2] == key:
#         print('查找成功！')
#         count += 1
#         print(count)
#     elif values[len(values)//2] > key:
#         new_values = []
#         for i in range(len(values)//2):
#             new_values.append(values[i])
#         count += 1
#         search_num(new_values, key, count)
#     else:
#         new_values = []
#         for i in range(len(values)//2 + 1, len(values)):
#             new_values.append(values[i])
#         count += 1
#         search_num(new_values, key, count)

# search_num(values, 22)


# def search_num2(values, key):
#     left = 0
#     right = len(values) - 1
#     while left <= right:
#         middle = (left + right) // 2
#         if values[middle] == key:
#             return middle
#         elif values[middle] > key:
#             right = middle - 1
#         else:
#             left = middle + 1

# print(search_num2(values, 10))


#3
import time
lst = [18, 8, 3, 14, 15, 10, 7, 19, 21, 4, 1, 20, 6, 16, 13, 11, 2, 17, 12, 5, 9]

def bubble(value):
    x = len(value)
    count = 0
    while count <= x:
        for i in range(x - 1):
            if value[i] > value[i+1]:
                value[i], value[i+1] = value[i+1], value[i]
        count += 1
    return value

print(bubble(lst))






























