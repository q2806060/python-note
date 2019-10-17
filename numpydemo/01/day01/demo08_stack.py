"""
demo08_stack.py   多维数组的组合与拆分
"""
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)

# 垂直方向的组合与拆分
c = np.vstack((a, b))
print(c, c.shape)
a, b = np.vsplit(c, 2)
print(a, b, sep='\n')

# 水平方向的组合与拆分
d = np.hstack((a, b))
print(d, d.shape)
a, b = np.hsplit(d, 2)
print(a, b, sep='\n')

# 深度方向的组合与拆分
e = np.dstack((a, b))
print(e, e.shape)
a, b = np.dsplit(e, 2)
print(a, b, sep='\n')

# 简单一维数组的组合方案
a = a.ravel()
b = b.ravel()
c = np.row_stack((a, b))
d = np.column_stack((a, b))
print(c)
print(d)






