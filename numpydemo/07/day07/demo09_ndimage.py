"""
demo09_ndimage.py  简单图像处理
"""
import numpy as np
import matplotlib.pyplot as mp
import scipy.misc as sm
import scipy.ndimage as sn

image=sm.imread('../da_data/lily.jpg', True)

# 高斯模糊
image2 = sn.median_filter(image, 5)
# 角度旋转
image3 = sn.rotate(image, 45)
# 边缘识别
image4 = sn.prewitt(image)

mp.figure('Ndimage')
mp.subplot(221)
mp.imshow(image, cmap='gray')
mp.axis('off')
mp.subplot(222)
mp.imshow(image2, cmap='gray')
mp.axis('off')
mp.subplot(223)
mp.imshow(image3, cmap='gray')
mp.axis('off')
mp.subplot(224)
mp.imshow(image4, cmap='gray')
mp.axis('off')
mp.show()
