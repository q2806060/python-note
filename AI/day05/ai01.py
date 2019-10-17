import numpy as np 
import sklearn.preprocessing as sp 
import sklearn.model_selection as ms 
import sklearn.svm as svm
import sklearn.metrics as sm 


class DigitEncoder():

    def fit_transform(self, y):
        return y.astype(int)

    def transform(self, y):
        return y.astype(int)

    def inverse_transform(self, y):
        return y.astype(str)

data = np.loadtxt('C:\\Users\\Administrator\\Desktop\\sucai\\ml_data\\traffic.txt', delimiter=',', dtype='U20')

data = data.T 
encoders, x = [], []

for row in range(len(data)):
    if data[row][0].isdigit():
        encoder = DigitEncoder()
    else:
        encoder = sp.LabelEncoder()
    encoders.append(encoder)

    if row < len(data)-1:
        x.append(encoder.fit_transform(data[row]))
    else:
        y = encoder.fit_transform(data[row])

x = np.array(x).T 

# 拆分测试集与训练集
train_x, test_x, train_y, test_y = ms.train_test_split(x, y, test_size=0.25, random_state=7)
# 创建模型，模型训练
model = svm.SVR(kernel='rbf', C=10)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
# 结果预测
