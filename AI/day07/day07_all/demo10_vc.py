"""
demo10_vc.py  捕获视频
"""
import cv2 as cv
# 获取视频采集设备   下标为0的摄像头
videoCapture = cv.VideoCapture(0)
# 获取采集到的第一张图片(第一帧)

while True:
	frame = videoCapture.read()[1]
	cv.imshow('frame', frame)
	# 每33毫秒自动解除阻塞
	if cv.waitKey(33) == 27:
		break

# 释放视频设备
videoCapture.release()
cv.destroyAllWindows()  # 销毁所有窗口




