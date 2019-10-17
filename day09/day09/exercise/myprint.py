# 思考题:
#   查看 >>> help(print)  猜想print 函数的参数列表是如何
#   定义的,能否自己实现一个myprint函数,代替print
#       (内都可以调用print来进行输出)
#   myprint / print(1,2,3,4)
#   myprint / print(1,2,3,4, sep="#")
#   myprint / print(1, 2, 3, 4, 5, end=' ')

def myprint(*args, sep=' ', end='\n'):
    # 设置一个标志,当第二次输出时,前要加sep作为分隔符
    flag = False  # 如果不是第一次输出,则此值为True
    for arg in args:
        s = str(arg)  # 将对象arg转为字符串,准备放在终端上
        if flag:
            print(sep, end='')
        print(s, end='')
        flag = True  # 标志,以后再打印,不再是第一次打印
    print(end, end='')

print(1,2,3,4)
print(1,2,3,4, sep="#")
print(1, 2, 3, 4, 5, end=' ')
print(1, 2, 3, 4, 5, end=' ', sep='%')
