"""
demo07_star.py star特征点检测
"""
import cv2 as cv
img = cv.imread('../ml_data/table.jpg')
cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
# 提取特征点
star = cv.xfeatures2d.StarDetector_create()
keypoints = star.detect(gray)
mixture = img.copy()
cv.drawKeypoints(img, keypoints, 
                 mixture, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('mixture', mixture)
cv.waitKey()
