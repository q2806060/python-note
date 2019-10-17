"""
demo05_eqhist.py  直方图均衡化 
"""
import cv2 as cv

img = cv.imread('../ml_data/sunrise.jpg')
cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
equalized_gray = cv.equalizeHist(gray)
cv.imshow('equalized_gray', equalized_gray)
# 对彩色图像提亮
# YUV: 亮度, 色度, 饱和度
yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
yuv[:,:,0] = cv.equalizeHist(yuv[:,:,0])
equalized_color = cv.cvtColor(yuv, cv.COLOR_YUV2BGR)
cv.imshow('equalized_color', equalized_color)

cv.waitKey()


