"""
demo03_cv.py  opencv基础
"""
import numpy as np
import cv2 as cv

# 读取图片并显示
img = cv.imread('../ml_data/forest.jpg')
cv.imshow('Image', img)
# 显示图像中每个颜色通道的图像
print(img.shape)
# 0 保留蓝色通道 其他颜色值为0
blue = np.zeros_like(img)
blue[:,:,0] = img[:,:,0]
cv.imshow('blue', blue)

# 1 保留绿色通道 其他颜色值为0
green = np.zeros_like(img)
green[:,:,1] = img[:,:,1]
cv.imshow('green', green)

# 2 保留红色通道 其他颜色值为0
red = np.zeros_like(img)
red[:,:,2] = img[:,:,2]
cv.imshow('red', red)

# 图像裁剪
h, w = img.shape[:2]
l, t = int(w/4), int(h/4)
r, b = int(w*3/4), int(h*3/4)
cropped = img[t:b, l:r]
cv.imshow('cropped', cropped)

# 图像缩放  
scaled = cv.resize(img, (int(w/4), int(h/4)), 
	interpolation=cv.INTER_LINEAR)
cv.imshow('scaled', scaled)

scaled2 = cv.resize(scaled, (w, h),
	interpolation=cv.INTER_LINEAR)
cv.imshow('scaled2', scaled2)

# 图像文件的保存
cv.imwrite('../ml_data/blue.jpg', blue)


cv.waitKey()  # 阻塞方法, 按下键盘继续执行
