"""
demo02_car.py  预测小汽车的等级
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms

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
model = se.RandomForestClassifier(max_depth=6, 
	n_estimators=200, random_state=7)
# 交叉验证
print(train_x.shape, train_y.shape)
score = ms.cross_val_score(model, train_x, 
	train_y, cv=4, scoring='f1_weighted')
print(score.mean())
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


