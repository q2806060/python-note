
#  3. 写一个函数input_number
#     def input_number():
#          ....
#     函数用来获取用户循环输入的整数,当用户输入负数时结束输入
#     将用户输入的数字以列表的形式返回,再用内建函数max,min
#     sum等求出用户输入的最大值,最小值及和
#     L = input_number()
#     print(L)
#     print("用户输入的最大值是:", max(L))
#     print("用户输入的最小值是:", min(L))
#     print("用户输入的数据之和是:", sum(L))



# 方法1
# def input_number():
#     lst = []  # 先创建一个列表,准备存放数据
#     while True:
#         x = int(input("请输入一个正数: "))
#         if x < 0:
#             break
#         lst.append(x)
#     return lst

# 方法2
def input_number():
    lst = []  # 先创建一个列表,准备存放数据
    while True:
        x = int(input("请输入一个正数: "))
        if x < 0:
            return lst
        lst.append(x)

L = input_number()
print(L)
print("用户输入的最大值是:", max(L))
print("用户输入的最小值是:", min(L))
print("用户输入的数据之和是:", sum(L))

    