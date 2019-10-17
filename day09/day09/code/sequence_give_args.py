

def myfun1(a, b, c):
    '''这是一个函数参数的示例'''
    print('a=', a)
    print('b=', b)
    print('c=', c)

s1 = [11, 22, 33]
s2 = (44, 55, 66)
s3 = "ABC"

myfun1(*s1)  #等同于 myfun1(s1[0], s1[1], s1[2])
myfun1(*s2)
myfun1(*s3)



