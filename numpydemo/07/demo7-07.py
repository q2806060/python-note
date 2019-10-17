import scipy.interpolate as si 
import numpy as np 
import matplotlib.pyplot as mp 


min_x = -50
max_x = 50
dis_x = np.linspace(min_x,max_x, 15)
dis_y = np.sinc(dis_x)

mp.figure('interpolate', facecolor='lightgray')
mp.title('Interpolate', fontsize=16)
mp.grid(linestyle=':')
mp.scatter(dis_x, dis_y, marker='D', c='red', label='Point')

# 通过这组散点，构建线型插值器函数
linear = si.interp1d(dis_x, dis_y)
lin_x = np.linspace(min_x, max_x, 1000)
lin_y = linear(lin_x)
mp.plot(lin_x, lin_y, c='dodgerblue', label='Linear Interpolate')

# 构建三次样条插值器
cubic = si.interp1d(dis_x, dis_y, kind='cubic')
cub_y = cubic(lin_x)
mp.plot(lin_x, cub_y, c='orangered', label='Cubic Interpolate')

mp.legend()
mp.show()