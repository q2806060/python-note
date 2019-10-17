"""
demo03_vc.py  验证曲线
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as mp

data = np.loadtxt('../ml_data/car.txt', 
	dtype='U20', delimiter=',')
data = data.T
encoders = []
train_x, train_y = [], []
for row in range(len(data)):
	# 创建适用于当前特征的标签编码器
	encoder = sp.LabelEncoder()
	if row < len(data)-1:
		train_x.append(
			encoder.fit_transform(data[row]))
	else:
		train_y = \
			encoder.fit_transform(data[row])
	encoders.append(encoder)
train_x = np.array(train_x).T

# 模型训练
'''
model = se.RandomForestClassifier(max_depth=6, 
	random_state=7)
# 输出验证曲线 选取最优:n_estimators
train_scores,test_scores=ms.validation_curve(
	model, train_x, train_y, 
	'n_estimators', np.arange(50,550,50),
	cv=5)

ne_scores = test_scores.mean(axis=1)
print(ne_scores)

mp.figure('VC')
mp.title('n_estimators Curve', fontsize=16)
mp.xlabel('n_estimators', fontsize=14)
mp.ylabel('score', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(linestyle=':')
mp.plot(np.arange(50,550,50), ne_scores,
	linewidth=2, c='dodgerblue', 
	label='n_estimators Curve')
mp.legend()
mp.show()


model = se.RandomForestClassifier(
	n_estimators=150, random_state=7)
# 输出验证曲线 选取最优:max_depth
train_scores,test_scores=ms.validation_curve(
	model, train_x, train_y, 
	'max_depth', np.arange(1, 11),
	cv=5)

md_scores = test_scores.mean(axis=1)
print(md_scores)

mp.figure('VC')
mp.title('max_depth Curve', fontsize=16)
mp.xlabel('max_depth', fontsize=14)
mp.ylabel('score', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(linestyle=':')
mp.plot(np.arange(1, 11), md_scores,
	linewidth=2, c='orangered', 
	label='max_depth Curve')
mp.legend()
mp.show()
'''

model = se.RandomForestClassifier(
	max_depth=9, n_estimators=150, 
	random_state=7)
model.fit(train_x, train_y)

# 自定义测试集  进行预测
data = [
['high','med','5more','4','big','low','unacc'],
['high','high','4','4','med','med','acc'],
['low','low','2','4','small','high','good'],
['low','med','3','4','med','high','vgood']]
# 训练时如何做的标签编码, 测试时需要使用相同的
# 标签编码器进行编码
data = np.array(data).T
test_x, test_y = [], []
for row in range(len(data)):
	encoder = encoders[row] # 得到标签编码器
	if row < len(data)-1:
		test_x.append(
			encoder.transform(data[row]))
	else:
		test_y = encoder.transform(data[row])
test_x = np.array(test_x).T
pred_test_y = model.predict(test_x)
enc = encoders[-1]
print(enc.inverse_transform(test_y))
print(enc.inverse_transform(pred_test_y))

