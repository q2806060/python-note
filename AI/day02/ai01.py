import numpy as np 
import matplotlib.pyplot as mp 
import mpl_toolkits.mplot3d as axes3d
import pickle

train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])

times = 1000        # 存储梯度下降的次数
rate = 0.01         # 记录每次梯度下降模型参数变化率
epoches = []        # 记录每次梯度下降的索引
w0, w1, losses = [1], [1], []
# 模拟梯度下降的过程
for i in range(1, times+1):
    epoches.append(i)
    loss = (((w0[-1] + w1[-1]*train_x) - train_y) ** 2).sum() / 2
    losses.append(loss)
    print('{:4}>w0={:.8f},w1={:.8f},loss={:.8f}'.format(epoches[-1], w0[-1], w1[-1], losses[-1]))

    # 根据偏导数公式，求得w0与w1方向上的梯度值
    d0 = ((((w0[-1] + w1[-1]*train_x) - train_y) ** 2).sum())
    d1 = (((w0[-1] + w1[-1]*train_x) - train_y)*train_x).sum()
    w0.append(w0[-1] - rate*d0)
    w1.append(w1[-1] - rate*d1)

pre_y = w0[-1] + w1[-1]*train_x
# 绘制训练数据
mp.figure("Linear Regression", facecolor='lightgray')
mp.figure('Linear Regression', fontsize=16)
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.scatter(train_x, train_y, marker='o', s=60, c='dodgerblue', label='Train Points')
mp.plot(train_x, pre_y, c=)
mp.legend()

# 绘制对着每次梯度下降过程，w0 w1 loss函数的变化
mp.figure("Training Progress", facecolor='lightgray')
mp.subplot(311)
mp.title("Training W0", fontsize=14)
mp.ylabel('w0', fontsize=12)
mp.grid(linestyle=':')
mp.tick_params(labelsize=10)
mp.plot(epoches, w0[:-1], c='dodgerblue', label='w0 Progress')
mp.legend()

# 在三维曲面中绘制梯度下降的过程
grid_w0, grid_w1 = np.meshgrid(np.linspace(0, 9, 500), np.linspace(0, 3.5, 500))
grid_loss = np.zeros_like(grid_w0)
for x, y in zip(train_x, train_y):
    grid_loss += (grid_w0 + x * grid_w1 - y) ** 2 / 2

mp.figure("Loss Function")
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('w0', fontsize=14)
ax3d.set_ylabel('w1', fontsize=14)
ax3d.set_zlabel('loss', fontsize=14)
ax.plot_surface(grid_w0, grid_w1, grid_loss, rstride=10, cstride=10, cmap='jet')
ax3d.plot(w0[:-1], w1[:-1], losses, 'o-', c='red', label='BGD')

mp.show()
