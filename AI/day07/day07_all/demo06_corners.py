"""
demo06_corners.py  角点检测
"""
import cv2 as cv

img = cv.imread('../ml_data/box.png')
cv.imshow('img', img)
# 角点监测
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
corners = cv.cornerHarris(gray, 7, 5, 0.04)
print(img.shape, corners.shape)
# 在图像中绘制角点
mixture = img.copy()
mixture[corners>corners.max()*0.01] = [0,0,255]
cv.imshow('mixture', mixture)

cv.waitKey()
