"""
demo03_vectorize.py 函数矢量化
"""
import numpy as np
import math as m

def f(a, b):
	r = m.sqrt(a**2 + b**2)
	return r
# 处理标量
print(f(3, 4))
# 处理矢量参数
a = np.array([3, 4, 5])
b = np.array([4, 5, 6])
# 把f函数矢量化
f_vec = np.vectorize(f)
print(f_vec(a, b))
print(np.vectorize(f)(a, b))

# 使用frompyfunc实现函数矢量化
# 2: 函数接收2个参数    1: 函数有1个返回值
f_func = np.frompyfunc(f, 2, 1)
print(f_func(a, b))