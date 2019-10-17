#   3. 看懂下面的程序在做什么?
#     def fx(f, x, y):
#         print(f(x, y))
    
#     fx((lambda a, b: a + b), 100, 200)
#     fx((lambda c, d: c ** d), 3, 4)


def fx(f, x, y):
    print(f(x, y))

fx((lambda a, b: a + b), 100, 200)
fx((lambda c, d: c ** d), 3, 4)

