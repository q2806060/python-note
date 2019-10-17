"""
demo07_mask.py  ndarray的掩码操作
"""
import numpy as np
a = np.arange(1, 10)
mask = (a%2==0)
print(a)
print(mask)
print(a[mask])
# 使用掩码对数组排序
mask = [8, 1, 2, 7, 3, 4, 6, 5, 0]
print(a[mask])

# 输出100以内3与7的倍数
b = np.arange(100)
print(b[(b%3==0) & (b%7==0)])
