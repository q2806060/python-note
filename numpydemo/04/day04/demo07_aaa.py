"""
demo07_aaa.py  测试数组轴向汇总相关API
"""
import numpy as np

ary = np.random.uniform(0, 10, (3, 5))
ary = ary.astype(int)
print(ary)
# 轴向汇总
def func(data):
	print('--',data)
	return data.mean(), data.max(), data.min()

r = np.apply_along_axis(func, 0, ary)
print(r)