"""
demo08_surface.py  三维曲面图
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

# 生成网格点坐标矩阵
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
				   np.linspace(-3, 3, n))
# 根据x,y 计算当前坐标下的z高度值
z = (1-x/2 + x**5 + y**3) * np.exp(-x**2 -y**2)

mp.figure('Surface', facecolor='lightgray')
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('X', fontsize=14)
ax3d.set_ylabel('Y', fontsize=14)
ax3d.set_zlabel('Z', fontsize=14)
ax3d.plot_surface(x, y, z, rstride=50, 
	cstride=50, cmap='jet')
mp.show()


