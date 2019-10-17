"""
demo05_shape.py  ndarray数组维度操作
"""
import numpy as np

a = np.arange(1, 9)
print(a)
# 视图变维
b = a.reshape(2, 4)
print(b)
b[0, 0] = 999
print(b)
c = a.ravel()
print(c)
c[1] = 888
print(c)
print(a)

# 复制变维  复制数据  b与d拥有独立数据
print('-' * 45)
d = b.flatten()
print(b)
print(d)
d[2] = 777
print(b)
print(d)


# 就地变维
print('-' * 45)
b.shape = (4, 2)
print(b)
b.resize(2, 2, 2)
print(b)









