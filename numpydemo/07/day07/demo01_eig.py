"""
demo01_eig.py 特征值与特征向量
"""
import numpy as np

A = np.mat('1 5 8; 2 5 7; 8 2 4')
# 提取特征值与特征向量
eigvals, eigvecs = np.linalg.eig(A)
print(eigvals)
print(eigvecs)
# 逆向推导原方阵
S = np.mat(eigvecs) * \
	np.mat(np.diag(eigvals)) * \
	np.mat(eigvecs).I
print(S)
eigvals[1:] = 0
S = np.mat(eigvecs) * \
	np.mat(np.diag(eigvals)) * \
	np.mat(eigvecs).I
print(S)