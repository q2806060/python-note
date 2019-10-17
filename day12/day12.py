#1

# def isou(x):
#     return x % 2 == 0

# print(list(filter(isou, range(1, 21))))


#2

# def recursion_myfac(n):
#     if n == 0:
#         return 1
#     s = recursion_myfac(n - 1)
#     r = n * s
#     print(r)
#     return r
# print(recursion_myfac(5))


#3

# def recursion_sum(n):
#     if n == 1:
#         return 1
#     s = recursion_sum(n - 1)
#     r = n + s
#     return r

# print(recursion_sum(5))

    
#4


# def age(n):
#     if n == 1:
#         return 10
#     age0 = age(n - 1)
#     ages = age0 + 2
#     return ages

# print(age(5))


# 练习


# def recursion_myfac(n):
#     if n == 0:
#         return 1
#     s = recursion_myfac(n - 1)
#     r = n * s
#     return r
# n = int(input('请输入一个整数：'))
# l = []
# for i in range(1, n + 1):
#     l.append(recursion_myfac(i))
# print(sum(l))

    
l = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
# def print_list(lst):
#     for i in lst:
#         if type(i) is list:
#             print_list(i)
#         else:
#             print(i)

# print_list(l)

# def sum_list(lst):
#     my_list = []    
#     def print_list(lst):
#         for i in lst:
#             if type(i) is list:
#                 print_list(i)
#             else:
#                 my_list.append(i)
#         return my_list
#     print_list(lst)
#     return sum(my_list)
# print(sum_list(l))
    
def sum_list(lst):
    s = 0
    for i in lst:
        if type(i) is int:
            s += i
        else:
            s += sum_list(i)
    return s
sum_list(l)













































































































