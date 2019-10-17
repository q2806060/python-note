"""
demo07_linear.py 线性回归
实现线性回归模型梯度下降过程
"""
import numpy as np
import matplotlib.pyplot as mp

train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])

times = 1000 # 存储梯度下降的次数
rate = 0.01 # 记录每次梯度下降模型参数变化率
epoches = [] # 记录每次梯度下降的索引
w0, w1, losses = [1], [1], []
# 模拟梯度下降的过程
for i in range(1, times+1):
	epoches.append(i)
	loss = ((w0[-1] + w1[-1]*train_x \
				- train_y) ** 2).sum() / 2
	# 根据偏导数公式, 求得w0与w1方向上的梯度值
	d0=((w0[-1]+w1[-1]*train_x)-train_y).sum()
	d1=(((w0[-1]+w1[-1]*train_x)-train_y)*\
			train_x).sum()
	w0.append(w0[-1] - rate*d0)
	w1.append(w1[-1] - rate*d1)
# 经过1000次下降,
# 最终得到的w0与w1使得loss函数值接近最小

pred_y = w0[-1] + w1[-1]*train_x

# 绘制训练数据
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=16)
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, marker='o',
	s = 60, c='dodgerblue', 
	label='Train Points')
mp.plot(train_x, pred_y, c='orangered',
	linewidth=2, label='Regression Line')
mp.legend()
mp.show()




