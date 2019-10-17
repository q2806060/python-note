"""
demo07_nb.py  朴素贝叶斯分类
"""
import numpy as np
import sklearn.naive_bayes as nb
import matplotlib.pyplot as mp

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
# 通过样本数据,训练朴素贝叶斯分类模型
model = nb.GaussianNB()
model.fit(x, y)
# 绘制分类边界线
l, r = x[:, 0].min()-1, x[:, 0].max()+1
b, t = x[:, 1].min()-1, x[:, 1].max()+1
n = 500
grid_x, grid_y = np.meshgrid(
	np.linspace(l, r, n),
	np.linspace(b, t, n))
test_x = np.column_stack(
	(grid_x.ravel(), grid_y.ravel()))
pred_test_y = model.predict(test_x)
grid_z = pred_test_y.reshape(grid_x.shape)
mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')


mp.scatter(x[:,0], x[:,1], s=60, c=y, 
	cmap='jet', label='Points')
mp.legend()
mp.show()



