"""
demo05_meanshift.py 均值漂移
"""
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp

x = np.loadtxt('../ml_data/multiple3.txt', 
	delimiter=',')

# 均值漂移实现聚类划分

bw = sc.estimate_bandwidth(
	x, n_samples=len(x), quantile=0.2)
model = sc.MeanShift(bandwidth=bw)

model.fit(x)
centers = model.cluster_centers_
print(centers)
pred_y = model.predict(x)
# 划分聚类边界
l, r = x[:, 0].min()-1, x[:, 0].max()+1
b, t = x[:, 1].min()-1, x[:, 1].max()+1
n = 500
grid_x, grid_y = np.meshgrid(
	np.linspace(l, r, n),
	np.linspace(b, t, n))
mesh_x = np.column_stack((grid_x.ravel(), 
	grid_y.ravel()))
pred_mesh_y = model.predict(mesh_x)
grid_z = pred_mesh_y.reshape(grid_x.shape)

mp.figure('MeanShift', facecolor='lightgray')
mp.title('MeanShift', fontsize=16)
mp.xlabel('X',fontsize=14)
mp.ylabel('Y',fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')
mp.scatter(x[:,0], x[:,1], c=pred_y, cmap='jet',
		label='points')
# 绘制聚类中心点
mp.scatter(centers[:,0], centers[:,1],
	marker='+', s=230, c='orangered')
mp.legend()
mp.show()



