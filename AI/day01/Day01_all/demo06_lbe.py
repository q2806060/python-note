"""
demo06_lbe.py  标签编码器
"""
import numpy as np
import sklearn.preprocessing as sp

samples = np.array(['audi', 'ford', 'audi',
	'toyota', 'ford', 'bmw', 'toyota',
	'ford', 'audi'])

# 标签编码器
lbe = sp.LabelEncoder()
r_samples = lbe.fit_transform(samples)
print(r_samples)

inv_samples = lbe.inverse_transform(r_samples)
print(inv_samples)