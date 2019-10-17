"""
demo08_dbscan.py dbscan算法
"""
import numpy as np
import sklearn.cluster as sc
import sklearn.metrics as sm
import matplotlib.pyplot as mp

x = np.loadtxt('../ml_data/perf.txt', 
		       delimiter=',')

# 准备训练模型相关数据
epsilons, scores, models = \
	np.linspace(0.3, 1.2, 10), [], []
# 遍历所有的半径, 训练模型, 查看得分
for epsilon in epsilons:
	model=sc.DBSCAN(eps=epsilon,min_samples=5)
	model.fit(x)
	score=sm.silhouette_score(x, model.labels_, 
		sample_size=len(x), metric='euclidean')
	scores.append(score)
	models.append(model)
# 转成ndarray数组
scores = np.array(scores)
best_i = scores.argmax() # 最优分数的索引
best_eps = epsilons[best_i]
best_sco = scores[best_i]
print(best_eps)
print(best_sco)
# 获取最优模型
best_model = models[best_i]

# 对输入x进行预测得到预测类别
pred_y = best_model.fit_predict(x)

# 获取孤立样本, 外周样本, 核心样本
core_mask = np.zeros(len(x), dtype=bool)
# 获取核心样本的索引, 把对应位置的元素改为True
core_mask[best_model.core_sample_indices_]=True
# 孤立样本的类别标签为-1
offset_mask = best_model.labels_ == -1
# 外周样本掩码 (不是核心也不是孤立样本)
p_mask = ~(core_mask | offset_mask)

# 绘制这些样本数据
mp.figure('DBSCAN cluster', facecolor='lightgray')
mp.title('DBSCAN cluster', fontsize=16)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
# 绘制核心样本
mp.scatter(x[core_mask][:,0], x[core_mask][:,1],
	s=60, cmap='brg', c=pred_y[core_mask])
# 绘制外周样本
mp.scatter(x[p_mask][:,0], x[p_mask][:,1],
	s=60, cmap='brg', c=pred_y[p_mask], 
	alpha=0.5)
# 绘制孤立样本
mp.scatter(x[offset_mask][:,0], 
	x[offset_mask][:,1], s=60, c='gray')

mp.show()








