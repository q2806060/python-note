import numpy as np 
import math as m 

def f(a, b):
    r = m.sqrt(a**2 + b**2)
    return r 

print(f(3, 4))
a = np.array([3, 4, 5])
b = np.array([4, 5, 6])

# 把f函数矢量化
f_vec = np.vectorize(f)

print(f_vec(a,  b))

# 使用frompyfunc实现函数矢量化
# 2：函数接受2个参数    1：函数有1个返回值
f_func = np.frompyfunc(f, 2, 1)
print(f_func(a, b))
