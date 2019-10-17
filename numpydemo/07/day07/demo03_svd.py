"""
demo03_svd.py 奇异值分解
"""
import numpy as np
import scipy.misc as sm
import matplotlib.pyplot as mp

image = sm.imread('../da_data/lily.jpg', True)
print(type(image), image.shape)

# 提取image矩阵的特征值与特征向量
eigvals, eigvecs = np.linalg.eig(image)
# 抹掉一部分特征值 重新生成新的图片
print(eigvals.shape)
eigvals[100:] = 0
S = np.mat(eigvecs) * \
	np.mat(np.diag(eigvals)) * \
	np.mat(eigvecs).I
S = S.real

# 奇异值分解 
U, s, V = np.linalg.svd(image)
S2 = np.mat(U)*np.mat(np.diag(s))*np.mat(V)
# 保留部分奇异值  生成图片
s[100:] = 0
S3 = np.mat(U)*np.mat(np.diag(s))*np.mat(V)

mp.figure('Lily Features',facecolor='lightgray')
mp.subplot(2,2,1)
mp.xticks([])
mp.yticks([])
mp.imshow(image, cmap='gray')
mp.subplot(2,2,2)
mp.xticks([])
mp.yticks([])
mp.imshow(S, cmap='gray')
mp.subplot(2,2,3)
mp.xticks([])
mp.yticks([])
mp.imshow(S2, cmap='gray')
mp.subplot(2,2,4)
mp.xticks([])
mp.yticks([])
mp.imshow(S3, cmap='gray')
mp.tight_layout()
mp.show()

