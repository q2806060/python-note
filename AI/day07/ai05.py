import cv2 as cv 

img = cv.imread('C:\\Users\\Administrator\\Desktop\\sucai\\ml_data\\box.png')

cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
corners = cv.cornerHarris(gray, 7, 5, 0.04)

# 在图像中绘制角点
mixture = img.copy()
mixture[corners>corners.max()*0.01] = [0, 0, 255]
cv.imshow('mixture', mixture)

cv.waitKey()