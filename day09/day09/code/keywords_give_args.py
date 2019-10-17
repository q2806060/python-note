

# 此示例示意关键传参 
def myfun1(a, b, c):
    '''这是一个函数参数的示例'''
    print('a=', a)
    print('b=', b)
    print('c=', c)

# 把 100, 200, 300 三个值传给 myfun1的a, b,c 
myfun1(c=300, b=200, a=100)
myfun1(b=20, c=30, a=10)

# myfun1(b=10, c=100)  # 出错



