"""
demo06_agglomerative_clustering.py 
凝聚层次算法
"""
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp
import sklearn.neighbors as nb

x = np.loadtxt('../ml_data/multiple3.txt', 
	delimiter=',')

# 凝聚层次实现聚类划分
model = sc.AgglomerativeClustering(
			n_clusters=4)
pred_y = model.fit_predict(x)

mp.figure('AgglomerativeClustering', facecolor='lightgray')
mp.title('AgglomerativeClustering', fontsize=16)
mp.xlabel('X',fontsize=14)
mp.ylabel('Y',fontsize=14)
mp.tick_params(labelsize=10)
mp.scatter(x[:,0], x[:,1], c=pred_y, cmap='jet',
		label='points')
mp.legend()


# 凝聚层次实现聚类划分 以连续性为条件
# 近邻筛选器
conn = nb.kneighbors_graph(
	   x, 10, include_self=False)
model = sc.AgglomerativeClustering(
			linkage='average',
			n_clusters=4, connectivity=conn)
pred_y = model.fit_predict(x)

mp.figure('AgglomerativeClustering2', facecolor='lightgray')
mp.title('AgglomerativeClustering2', fontsize=16)
mp.xlabel('X',fontsize=14)
mp.ylabel('Y',fontsize=14)
mp.tick_params(labelsize=10)
mp.scatter(x[:,0], x[:,1], c=pred_y, cmap='jet',
		label='points')
mp.legend()


mp.show()




