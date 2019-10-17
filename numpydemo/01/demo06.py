import numpy as np 

a = np.arange(1,10)
# 利用掩码进行筛选
mask = (a%2==0)
print(mask)
print(a[mask])
# 利用下标进行排序
mask = [8,1,2,7,5,6,4,3,0]
print(a[mask])

b = np.arange(100)
mask = ((b%3==0) & (b%7==0))
print(b[mask])