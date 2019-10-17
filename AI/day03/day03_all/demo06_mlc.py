"""
demo06_mlc.py  多元逻辑分类  
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm

x = np.array([
	[4, 7],
	[3.5, 8],
	[3.1, 6.2],
	[0.5, 1],
	[1, 2],
	[1.2, 1.9],
	[6, 2],
	[5.7, 1.5],
	[5.4, 2.2]])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])
# 把样本绘制出来
mp.figure('Logistic Classification', facecolor='lightgray')
mp.title('Logistic Classification', fontsize=16)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

# 绘制分类边界线
l, r = x[:, 0].min()-1, x[:, 0].max()+1
b, t = x[:, 1].min()-1, x[:, 1].max()+1
n = 500
grid_x, grid_y = np.meshgrid(
	np.linspace(l, r, n),
	np.linspace(b, t, n))

# 构建逻辑分类器
model = lm.LogisticRegression(
	solver='liblinear', C=1000)
model.fit(x, y)
# 把grid_x与grid_y抻平了组成模型的输入,预测输出
test_x = np.column_stack(
	(grid_x.ravel(), grid_y.ravel()))
pred_test_y = model.predict(test_x)
grid_z = pred_test_y.reshape(grid_x.shape)

mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')

mp.scatter(x[:, 0], x[:, 1], s=60, c=y,
	marker='o', label='Points', cmap='jet')

mp.legend()
mp.show()


