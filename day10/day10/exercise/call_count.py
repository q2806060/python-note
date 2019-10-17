# 练习:
#   用全局变量记录一个函数hello被调用的次数,部分代码如下:
#     count = 0
#     def hello(....):
#         ...
#     hello("小张")  # 打印:你好,小张
#     hello("小李")  # 打印:你好,小李
#     print("hello这个函数被调用", count, '次')


count = 0
def hello(name):
    print("你好,", name)
    global count
    count += 1

hello("小张")  # 打印:你好,小张
hello("小李")  # 打印:你好,小李
print("hello这个函数被调用", count, '次')

