# 思考题:
#   查看 >>> help(print)  猜想print 函数的参数列表是如何
#   定义的,能否自己实现一个myprint函数,代替print
#       (内都可以调用print来进行输出)
#   myprint / print(1,2,3,4)
#   myprint / print(1,2,3,4, sep="#")
#   myprint / print(1, 2, 3, 4, 5, end=' ')

def myprint(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end)  # 拆开元组

myprint(1,2,3,4)
myprint(1,2,3,4, sep="#")
myprint(1, 2, 3, 4, 5, end=' ')
myprint(1, 2, 3, 4, 5, end=' ', sep='%')
