"""
demo02_eig.py 提取图片的特征值
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
eigvals[130:] = 0
S = np.mat(eigvecs) * \
	np.mat(np.diag(eigvals)) * \
	np.mat(eigvecs).I
S = S.real
mp.figure('Lily Features',facecolor='lightgray')
mp.subplot(1,2,1)
mp.xticks([])
mp.yticks([])
mp.imshow(image, cmap='gray')
mp.subplot(1,2,2)
mp.xticks([])
mp.yticks([])
mp.imshow(S, cmap='gray')
mp.tight_layout()
mp.show()

