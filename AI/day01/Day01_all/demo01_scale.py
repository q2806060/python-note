"""
demo01_scale.py 均值移除
"""
import numpy as np
import sklearn.preprocessing as sp

samples = np.array([
		[17., 100., 4000],
		[20., 80.,  5000],
		[23., 70.,  5500]])

return_samples = sp.scale(samples)
print(return_samples)
print(np.mean(return_samples, axis=0))
print(np.std(return_samples, axis=0))
