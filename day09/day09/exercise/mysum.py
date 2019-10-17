
# 练习:
#   写一个函数mysum 可以传入任意个实参的数字,返回所有实参的和
#     def mysum(*args):
#        ....
#     print(mysum())  # 0
#     print(mysum(1, 2, 3, 4))  # 10
#     要求: 不允许调用内建函数sum



def mysum(*args):
    s = 0
    for x in args:
        s += x
    return s

print(mysum())  # 0
print(mysum(1, 2, 3, 4))  # 10


