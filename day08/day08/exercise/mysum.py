#   2. 写一个函数 mysum, 实现给出两个数,返回这两个数的和
#     def mysum(x, y):
#        ...
#     a = int(input("请输入第一个数: "))
#     b = int(input("请输入第二个数: "))
#     print("您输入的两个数的和是:", mysum(a, b))



def mysum(x, y):
    s = x + y
    return s   # return x + y

a = int(input("请输入第一个数: "))
b = int(input("请输入第二个数: "))
print("您输入的两个数的和是:", mysum(a, b))