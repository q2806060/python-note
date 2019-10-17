import numpy as np

a = np.arange(1,10,1)
print(a, a.shape)
a.shape = (3,3)
print(a)

print(a.dtype)
b = a.astype(float)
print(b, b.dtype)

b[0][0] = 999
print(b)

print(a.size)
print(b.size)
print(len(a))
print(len(b))

c = np.arange(1,19).reshape(3,2,3)
print(c)
print(c[0,0,0])

for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        for k in range(c.shape[2]):
            print(c[i,j,k],end=" ")