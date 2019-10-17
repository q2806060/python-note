#   2. 写一个lambda表达式来创建函数,此函数返回两个形参变量的
#     最大值:
#     def mymax(x, y):
#         ....
#     mymax = lambda .....
#     print(mymax(100, 200))  # 200
#     要求: 尽可能不调用max函数



# def mymax(x, y):
#     if x > y:
#         return x
#     else:
#         return y

mymax = lambda x, y: x if x > y else y
print(mymax(100, 200))  # 200
