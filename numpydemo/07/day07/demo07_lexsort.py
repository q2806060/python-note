"""
demo07_lexsort.py  联合间接排序
"""
import numpy as np

# 为商品排序.   价格  ->  销量
p = np.array(['Apple','HuaWei','OPPO','MI','VIVO'])
prices = [8888, 4500, 3999, 2999, 3999]
totals = np.array([100, 200, 99, 110, 80])

indices = np.lexsort((totals*-1, prices))
print(p[indices])


a = np.array([1, 2, 4, 6, 8])
b = np.array([3, 5])
indices = np.searchsorted(a, b)
print(indices)
a = np.insert(a, indices, b)
print(a)