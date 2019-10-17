import cv2 as cv 

img = cv.imread('C:\\Users\\Administrator\\Desktop\\sucai\\ml_data\\chair.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('img', img)

# canny边缘检测
canny = cv.Canny(img, 50, 240)
cv.imshow('canny', canny)



cv.waitKey()