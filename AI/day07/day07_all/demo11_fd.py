"""
demo11_fd.py  人脸定位器
"""
import cv2 as cv

fd = cv.CascadeClassifier('../ml_data/haar/face.xml')
ed = cv.CascadeClassifier('../ml_data/haar/eye.xml')
nd = cv.CascadeClassifier('../ml_data/haar/nose.xml')

# 获取视频采集设备   下标为0的摄像头
videoCapture = cv.VideoCapture(0)
# 获取采集到的第一张图片(第一帧)
while True:
	frame = videoCapture.read()[1]
	# 通过哈尔定位器 进行局部定位 并在图像中标注
	faces = fd.detectMultiScale(frame, 1.3, 2)
	for l, t, w, h in faces:
		# 绘制椭圆
		a, b = int(w/2), int(h/2)
		cv.ellipse(frame, 
			(l+a, t+b), # 椭圆心坐标
			(a, b), # 椭圆半径
			0, 0, 360, (255,0,255), 
			2 # 椭圆的线宽
		)
		# 绘制鼻子和眼睛
		face = frame[t:t+h, l:l+w]
		eyes = ed.detectMultiScale(face, 1.3, 5)
		for l, t, w, h in eyes:	
			a, b = int(w/2), int(h/2)
			cv.ellipse(face, 
				(l+a, t+b), # 椭圆心坐标
				(a, b), # 椭圆半径
				0, 0, 360, (0,255,255), 
				2 # 椭圆的线宽
			)
		
		nodes = nd.detectMultiScale(face, 1.3, 5)
		for l, t, w, h in nodes:	
			a, b = int(w/2), int(h/2)
			cv.ellipse(face, 
				(l+a, t+b), # 椭圆心坐标
				(a, b), # 椭圆半径
				0, 0, 360, (255,255,0), 
				2 # 椭圆的线宽
			)
	cv.imshow('frame', frame)
	# 每33毫秒自动解除阻塞
	if cv.waitKey(33) == 27:
		break

# 释放视频设备
videoCapture.release()
cv.destroyAllWindows()  # 销毁所有窗口




