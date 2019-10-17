import numpy as np 
import scipy.misc as sm 
import scipy.ndimage as sn 
import sklearn.cluster as sc 
import matplotlib.pyplot as mp 

img= sm.imread('C:\\Users\\Administrator\\Desktop\\sucai\\da_data\\lily.jpg', True)
# 图像量化
x = img.reshape(-1, 1)
model = sc.KMeans(n_clusters=4)
model.fit(x)
y = model.labels_
# 把每隔亮度值修改为响应的聚类中心值
centers = model.cluster_centers_.ravel()
result = centers[y].reshape(img.shape)
# y = model.predict(x)
# y = y.reshape(img.shape)

mp.figure('Image')
mp.subplot(121)
mp.yticks([])
mp.xticks([])
mp.imshow(result, cmap='gray')
mp.subplot(122)
mp.yticks([])
mp.xticks([])
mp.imshow(img, cmap='gray')
mp.tight_layout()
mp.show()