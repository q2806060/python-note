"""
demo04_canny.py  边缘检测
"""
import cv2 as cv
img = cv.imread('../ml_data/chair.jpg', 
				cv.IMREAD_GRAYSCALE)
cv.imshow('img', img)
# canny边缘检测
canny = cv.Canny(img, 50, 240)
cv.imshow('canny', canny)

# cv.Sobel() 索贝尔边缘检测
hsobel=cv.Sobel(img, cv.CV_64F, 1, 1, ksize=5)
cv.imshow('hsobel', hsobel)

cv.waitKey()