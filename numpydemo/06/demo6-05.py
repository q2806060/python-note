import numpy as np 

ary = np.arange(1, 10).reshape(3, 3)
m = np.matrix(ary, copy=True)
m[0, 0] = 999
print(m)
print(ary)

m2 = np.mat(ary)
m2[0, 0] = 888
print(m2)
print(ary)

m3 = np.mat('1 2 3; 4 5 6')
print(m3)

m3 = np.mat('1 2 3; 4 5 6')
print(m3)
print(m3.I)
print(m3*m3.I)