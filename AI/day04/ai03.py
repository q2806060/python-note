import numpy as np 
import sklearn.model_selection as ms 
import sklearn.svm as svm 
import sklearn.metrics as sm 
import matplotlib.pyplot as mp 

x, y = [], []

data = np.loadtxt('C:\\Users\\Administrator\\Desktop\\sucai\\ml_data\\multiple2.txt', delimiter=',')

x = data[:, :-1]
y = data[:, -1]
# 拆分训练集和测试集
train_x, test_x, train_y, test_y = ms.train_test_split(x, y, test_size=0.25, random_state=5)

# 基于线型核函数的svm绘制分类边界
model = svm.SVC(kernel='linear')
model.fit(train_x, train_y)

# 绘制这些点
mp.figure('SVM', facecolor='lightgray')
mp.title('SVM', fontsize=16)
mp.xlabel('X', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.scatter(x[:, 0], x[:, 1], s=60, c=y, label='points', cmap='jet')
mp.legend()
mp.show()