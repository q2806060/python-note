"""
demo02_ndarray.py
"""
import numpy as np
a = np.array([[1, 2, 3, 4], 
		      [5, 6, 7, 8]])
print(a, a.shape)
# 起始值1, 终止值10, 步长1
b = np.arange(1, 10, 2)
print(b)

# 创建5个元素全为0的数组
c = np.zeros(5, dtype='int32')
print(c, c.dtype)

# 创建5个元素全为1的数组
d = np.ones(5, dtype='int32')
print(d, d.dtype)
# 创建数组e与f, 结构与a相同, e中全0, f中全1
e = np.zeros_like(a)
f = np.ones_like(a)
print(e)
print(f / 5)





