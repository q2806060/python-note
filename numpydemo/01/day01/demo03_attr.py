"""
demo03_attr.py
"""
import numpy as np

# 测试数组的维度
a = np.arange(1, 10)
print(a, a.shape)
a.shape = (3, 3)
print(a, a.shape)

# 测试元素的类型
print(a.dtype)
b = a.astype(float)
print(b, b.dtype)

b[0][0] = 999
print(b)
print(a)

# 测试元素的个数
print('a.size:', a.size, 'len(a):', len(a))

# 数组元素的索引
c = np.arange(1, 19).reshape(3, 2, 3)
print(c)
print(c[0])
print(c[0][0])
print(c[0][0][0])
print(c[0, 0, 0])

# 遍历c中的每个元素并输出
for i in range(c.shape[0]):
	for j in range(c.shape[1]):
		for k in range(c.shape[2]):
			print(c[i,j,k], end=' ')