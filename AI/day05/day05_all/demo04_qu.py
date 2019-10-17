"""
demo04_qu.py  图像量化  KMeans聚类
"""
import numpy as np
import scipy.misc as sm
import scipy.ndimage as sn
import sklearn.cluster as sc
import matplotlib.pyplot as mp

img = sm.imread('../ml_data/lily.jpg', True)
# 图像量化
x = img.reshape(-1, 1)
model = sc.KMeans(n_clusters=2)
model.fit(x)
y = model.labels_
print(y.shape)
# 把每个亮度值修改为相应的聚类中心值
centers = model.cluster_centers_.ravel()
print(centers.shape, centers)
# 使用numpy的掩码操作 修改y数组的每个值
result = centers[y].reshape(img.shape)
mp.figure('Image')
mp.subplot(121)
mp.xticks([])
mp.yticks([])
mp.imshow(img, cmap='gray')
mp.subplot(122)
mp.xticks([])
mp.yticks([])
mp.imshow(result, cmap='gray')
mp.tight_layout()
mp.show()


