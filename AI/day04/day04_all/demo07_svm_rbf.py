"""
demo07_svm_rbf.py  支持向量机  径向基核函数
"""
import numpy as np
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import matplotlib.pyplot as mp

x, y = [],[]
data=np.loadtxt('../ml_data/multiple2.txt', 
	 delimiter=',')
x = data[:, :-1]
y = data[:, -1]
# 拆分训练集与测试集
train_x, test_x, train_y, test_y = \
	ms.train_test_split(x, y, test_size=0.25,
	random_state=5)
# 基于多项式核函数的svm绘制分类边界
model=svm.SVC(kernel='rbf', C=600, gamma=0.01)
model.fit(train_x, train_y)

# 绘制分类边界线
l, r = x[:, 0].min()-1, x[:, 0].max()+1
b, t = x[:, 1].min()-1, x[:, 1].max()+1
n = 500
grid_x, grid_y = np.meshgrid(
	np.linspace(l, r, n),
	np.linspace(b, t, n))
# 把grid_x与grid_y抻平了组成模型的输入,预测输出
mesh_x = np.column_stack(
	(grid_x.ravel(), grid_y.ravel()))
pred_mesh_y = model.predict(mesh_x)
grid_z = pred_mesh_y.reshape(grid_x.shape)

# 看一看测试集的分类报告
pred_test_y = model.predict(test_x)
cr = sm.classification_report(
	  	test_y, pred_test_y)
print(cr)

# 绘制这些点
mp.figure('SVM', facecolor='lightgray')
mp.title('SVM', fontsize=16)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')

mp.scatter(x[:,0], x[:,1], s=60, 
		c=y, label='points', cmap='jet')

mp.legend()
mp.show()








