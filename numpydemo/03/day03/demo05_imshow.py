"""
demo05_imshow.py  热成像图
"""
import numpy as np
import matplotlib.pyplot as mp

# 生成网格点坐标矩阵
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
				   np.linspace(-3, 3, n))
# 根据x,y 计算当前坐标下的z高度值
z = (1-x/2 + x**5 + y**3) * np.exp(-x**2 -y**2)

mp.figure('Imshow', facecolor='lightgray')
mp.title('Imshow', fontsize=18)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.imshow(z, cmap='jet', origin='lower')
mp.show()