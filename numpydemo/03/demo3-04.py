import numpy as np 
import matplotlib.pyplot as mp 

# 生成网格点坐标矩阵
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3,n), np.linspace(-3, 3, n))

# 根据x, y计算当前坐标下的z高度值
z = (1-x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

mp.figure("Contour", facecolor="lightgray")
mp.title("Contour", fontsize=18)
mp.xlabel("X", fontsize=14)
mp.ylabel("Y", fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
cntr = mp.contour(x, y, z, colors="black", linewidths=0.5)
# cntr等高线对象绘制标注
mp.clabel(cntr, inline_spacing=1, fmt='%.1f', fontsize=10)
# 等高线填充颜色
mp.contourf(x, y, z, 8,cmap='jet')
mp.show()