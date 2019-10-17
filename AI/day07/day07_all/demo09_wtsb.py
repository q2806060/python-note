"""
demo09_wtsb.py   物体识别
"""
import os 
import numpy as np
import hmmlearn.hmm as hl
import cv2 as cv

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


train_samples = \
	search_files('../ml_data/objects/training')

# 整理训练集, 把每一个类别中的图片的desc
# 摞在一起, 基于隐马模型开始训练.

train_x, train_y = [], []
for label, filenames in train_samples.items():
	descs = np.array([])
	for filename in filenames:
		# 获取当前图片的desc描述矩阵加入descs
		img = cv.imread(filename)
		gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
		# 对图片进行范围缩放
		h, w = gray.shape[:2]
		f = 200 / min(h, w)
		# fx: x轴伸缩比例  fy: y轴伸缩比例
		gray = cv.resize(gray, None, fx=f, fy=f)
		sift = cv.xfeatures2d.SIFT_create()
		keypoints = sift.detect(gray)
		_,desc = sift.compute(gray, keypoints)
		print(label, desc.shape)
		if len(descs) == 0:
			descs = desc
		else:
			descs = np.append(descs, desc, axis=0)
	train_x.append(descs)
	train_y.append(label)

# 基于隐马模型进行训练, 把所有类别的模型都存起来
# 一共3个类别循环3次
models = {}
for descs, label in zip(train_x, train_y):
	model = hl.GaussianHMM(n_components=4, 
		covariance_type='diag', n_iter=200)
	models[label] = model.fit(descs)

# 读取测试集中的文件, 使用每个模型对文件进行
# 评分, 取分值大的模型对应的label作为预测类别
test_samples = \
	search_files('../ml_data/objects/testing')

# 整理测试集, 提取每一个文件的mfcc
test_x, test_y = [], []
for label, filenames in test_samples.items():
	descs = np.array([])
	for filename in filenames:
		# 获取当前图片的desc描述矩阵加入descs
		img = cv.imread(filename)
		gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
		# 对图片进行范围缩放
		h, w = gray.shape[:2]
		f = 200 / min(h, w)
		# fx: x轴伸缩比例  fy: y轴伸缩比例
		gray = cv.resize(gray, None, fx=f, fy=f)
		sift = cv.xfeatures2d.SIFT_create()
		keypoints = sift.detect(gray)
		_,desc = sift.compute(gray, keypoints)
		print(label, desc.shape)
		if len(descs) == 0:
			descs = desc
		else:
			descs = np.append(descs, desc, axis=0)
	test_x.append(descs)
	test_y.append(label)

# 使用3个模型, 对每一个文件进行预测得分.
pred_test_y = []
# test_x一共3个样本, 遍历3次, 每次验证1个文件
for descs in test_x:
	best_score, best_label = None, None
	for label, model in models.items():
		score = model.score(descs)
		if (best_score is None) or \
					(best_score < score):
			best_score, best_label=score,label
	pred_test_y.append(best_label)

print(test_y)
print(pred_test_y)

