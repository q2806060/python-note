"""
demo06_slice.py  数组切片
"""
import numpy as np
a = np.arange(1, 10)
print(a)  # 1 2 3 4 5 6 7 8 9
print(a[:3])
print(a[3:6])
print(a[6:])
print(a[::-1])
print(a[:-4:-1])
print(a[-4:-7:-1])
print(a[-7::-1])
print(a[:])
print(a[::3])
print(a[1::3])