"""
demo05_matrix.py 
"""
import numpy as np

ary = np.arange(1, 10).reshape(3, 3)
m = np.matrix(ary, copy=True)
m[0,0]=999
print(m)
print(ary)
# 等价于np.matrix(ary, copy=False)
m2 = np.mat(ary)
m2[0,0] = 888
print(m2)
print(ary)

m3 = np.mat('1 2 3; 4 5 6')
print(m3)
print(m3 * 10)
print(m3 * m3.T)
print(m3.T * m3)

print('-' * 45)
m = np.mat('1 2 3; 5 4 3; 1 6 3')
m = np.mat('1 2 3; 4 5 3; 7 8 9')
print(m)
# print(m.I)
print(np.linalg.inv(m))
print(m * m.I)

print('-' * 45)
m = np.mat('1 2 3; 5 4 3')
print(m)
print(m.I)
# print(np.linalg.inv(m))
print(m * m.I)
