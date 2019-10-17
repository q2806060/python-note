"""
demo08_ms.py  训练集测试集划分
"""
import numpy as np
import sklearn.naive_bayes as nb
import matplotlib.pyplot as mp
import sklearn.model_selection as ms

data = np.loadtxt('../ml_data/multiple1.txt', 
	unpack=False, delimiter=',')
print(data.shape, data.dtype)
# 获取输入与输出
x = np.array(data[:, :-1])
y = np.array(data[:, -1])

# 绘制这些点, 点的颜色即是点的类别
mp.figure('Naive Bayes', facecolor='lightgray')
mp.title('Naive Bayes', fontsize=16)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.tick_params(labelsize=10)

# 训练集测试集划分
train_x, test_x, train_y, test_y = \
	ms.train_test_split(
	x, y, test_size=0.25, random_state=7)

# 通过训练样本,训练朴素贝叶斯分类模型
model = nb.GaussianNB()
# 到底用不用这个模型呢? 交叉验证看一下分数吧
score = ms.cross_val_score(
	model, train_x, train_y, cv=5, 
	scoring='accuracy')
print('CV Accuracy:', score)


model.fit(train_x, train_y)
# 对测试样本进行预测, 输出预测精确度
pred_test_y = model.predict(test_x)
# 精确度 = 预测正确的个数/总个数
print((test_y==pred_test_y).sum()/test_y.size)


# 绘制分类边界线
l, r = x[:, 0].min()-1, x[:, 0].max()+1
b, t = x[:, 1].min()-1, x[:, 1].max()+1
n = 500
grid_x, grid_y = np.meshgrid(
	np.linspace(l, r, n),
	np.linspace(b, t, n))
mesh_x = np.column_stack(
	(grid_x.ravel(), grid_y.ravel()))
pred_mesh_y = model.predict(mesh_x)
grid_z = pred_mesh_y.reshape(grid_x.shape)
mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')


mp.scatter(test_x[:,0], test_x[:,1], s=60, 
	c=test_y, cmap='jet', label='Train Points')
mp.legend()
mp.show()



