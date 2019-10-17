#1

# def get_score():
#     s = int(input('请输入成绩（0-100）：'))
#     print(s)

# try:
#     get_score()
# except ValueError:
#     print(0)


#2


# def get_age():
#     try:
#         age = int(input('请输入年龄（1-140）：'))
#         if 1 <= age <= 140:
#             print('用户的年龄是：', age)
#         else:
#             raise ValueError('您输入的不在范围内！')
#     except ValueError as err:
#         print('获取年龄时发生错误，错误原因是：', err)

# get_age()


# 练习


# s = {'唐僧', '悟空', '八戒', '沙僧'}
# peo = iter(s)
# while True:
#     try:
#         print(next(peo))
#     except StopIteration:
#         break




# def high(n, h):
#     h = h / 2
#     if n == 1:
#         return h 
#     h = high(n - 1, h)
#     return h
# print(high(10, 100))
# H = 0
# for i in range(1, 11):
#     H += high(i, 100) * 2

# s = 100 + H - high(10, 100)
# print(s)





























































































