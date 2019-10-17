"""
demo11_event.py 事件预测
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.svm as svm

# 模仿LabelEncoder的接口 设计数字编码器
class DigitEncoder():

    def fit_transform(self, y):
        return y.astype(int)

    def transform(self, y):
    	return y.astype(int)

    def inverse_transform(self, y):
    	return y.astype(str)

data = np.loadtxt('../ml_data/events.txt', 
       delimiter=',', dtype='U20')
# 转置后删掉1列
data = np.delete(data.T, 1, axis=0)
# 整理训练集
encoders, x = [], [] 
for row in range(len(data)):
	# 选择编码器, 如果是数字,则用自定义编码器
	if data[row][0].isdigit():
		encoder = DigitEncoder()
	else:
		encoder = sp.LabelEncoder()

	encoders.append(encoder)

	if row < len(data)-1: 
		x.append(
    		encoder.fit_transform(data[row]))
	else:
		y = encoder.fit_transform(data[row])

x = np.array(x).T
# 拆分训练集与测试集
train_x, test_x, train_y, test_y = \
    ms.train_test_split(x, y, test_size=0.25,
	random_state=7)
# 选择模型, 开始训练
model = svm.SVC(kernel='rbf', 
			    class_weight='balanced')
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
# 输出精确度
print((pred_test_y==test_y).sum()/test_y.size)


# 模拟接收参数: 预测输入  从而预测输出
data = [['Monday','13:30:00','22','31']]
data = np.array(data).T
x = []
for row in range(len(data)):
	encoder = encoders[row]
	x.append(encoder.transform(data[row]))
x = np.array(x).T
pred_y = model.predict(x)
print(encoders[-1].inverse_transform(pred_y))

