"""
demo12_face.py  人脸识别
"""
import os 
import numpy as np
import cv2 as cv
import sklearn.preprocessing as sp

fd = cv.CascadeClassifier('../sucai/ml_data/face.xml')

def search_files(directory):
	directory = os.path.normpath(directory)

	# {'apple':[dir,dir,dir], 'banana':[dir..]}
	objects = {}
	#当前目录, 当前目录子目录, 文件列表
	for curdir,subdirs,files in \
					os.walk(directory):
		for file in files:
			if file.endswith('.jpg'):
				label = curdir.split(os.path.sep)[-1]
				if label not in objects:
					objects[label] = []
				path = os.path.join(curdir, file)
				objects[label].append(path)
	return objects

# 训练的脸图片路径
train_faces = search_files(
		'../sucai/ml_data/faces/training')
# 类别名称标签编码器
codec = sp.LabelEncoder()
codec.fit(list(train_faces.keys()))

train_x = []
train_y = []
for label, filenames in train_faces.items():
	for filename in filenames:
		img = cv.imread(filename)
		gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
		faces = fd.detectMultiScale(img, 1.1, 2, minSize=(100,100))
		# 把这张脸加入训练集的输入 label作为样本的输出
		for l, t, w, h in faces:
			train_x.append(gray[t:t+h,l:l+w])
			train_y.append(codec.transform([label])[0])

train_y = np.array(train_y)
# 基于局部二值模式直方图做人脸识别模型
model = cv.face.LBPHFaceRecognizer_create()
model.train(train_x, train_y)
#模型训练完毕  模型预测


# 训练的脸图片路径
test_faces = search_files(
		'../sucai/ml_data/faces/testing')

test_x = []
test_y = []
for label, filenames in test_faces.items():
	for filename in filenames:
		img = cv.imread(filename)
		gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
		faces = fd.detectMultiScale(gray, 1.1, 2,
			minSize=(100, 100))
		# 把这张脸加入训练集的输入 label作为样本的输出
		for l, t, w, h in faces:
			test_x.append(gray[t:t+h,l:l+w])
			test_y.append(codec.transform([label])[0])

# 模型预测
pred_test_y = []
for face in test_x:
	pred_code = model.predict(face)[0]
	pred_test_y.append(pred_code)

print(test_y)
print(codec.transform(pred_test_y))