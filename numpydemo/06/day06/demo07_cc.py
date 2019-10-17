"""
demo07_cc.py  数组的常用函数
"""
import numpy as np

a = np.arange(1, 10)
# 数组裁剪: 最小值不小于下限, 最大值不大于上限
print(a.clip(min=3, max=6))
print(a.compress(a>=6))

print('-' * 45)
a = a.reshape(3, 3)
b = a[::]
print(np.add(a, b))
a = a.ravel()
print(a)
print(np.add.reduce(a))  # 求a元素的累加和
print(np.add.accumulate(a)) # a累加和的过程
print(np.add.outer([10,20], a)) # 外和

print('-' * 45)
print(a)
print(a.prod(), np.prod(a))
print(a.cumprod())
a = np.array([20, 20, -20, -20])
b = np.array([3, -3, 6, -6])
print(a/b, np.divide(a, b))
print(np.floor_divide(a, b))
print(np.ceil(a/b))
print(np.round(a/b))
print(np.trunc(a/b))

print('-' * 45)
print(a)
print(b)
print(a^b < 0)   # 判断是否异号
print(np.bitwise_xor(a,b) < 0)   # 判断是否异号

print('-' * 45)
for i in range(1000):
	if i & (i-1) == 0:
		print(i, end=' ')

a = np.arange(1, 1000)
print(a[a&(a-1) == 0])



