"""
demo02_plot.py  绘制一条正弦曲线
"""
import numpy as np
import matplotlib.pyplot as mp

# [-π,π] 拆1000个点
x = np.linspace(-np.pi, np.pi, 1000)
sin_x = np.sin(x)
# 绘制余弦曲线 y=1/2 * cos(x)
cos_x = np.cos(x) / 2
# 绘图
mp.plot(x, sin_x, linestyle='--', linewidth=2, 
		color='dodgerblue', alpha=0.9,
		label=r'$y=sin(x)$')
mp.plot(x, cos_x, linestyle=':', linewidth=3,
	    color='orangered', alpha=0.9,
	    label=r'$y=\frac{1}{2}cos(x)$')
# 修改可视范围
# mp.xlim(0, np.pi)
# mp.ylim(0, 1)

# 修改坐标刻度
x_val_list=[-np.pi, -np.pi/2, 0, np.pi/2, np.pi]
x_text_list=['-π', r'$-\frac{\pi}{2}$', '0', 
			 r'$\frac{π}{2}$', 'π']
mp.xticks(x_val_list, x_text_list)
mp.yticks([-1, -0.5, 0.5, 1], 
	      ['-1', '-0.5', '0.5', '1'])

# 设置坐标轴
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))

# 绘制两个特殊点
mp.scatter([np.pi/2, np.pi/2], [0, 1], 
	marker='X', s=80, edgecolor='dodgerblue',
	facecolor='deepskyblue', zorder=3)

# 为点添加备注
ap = dict(arrowstyle='->', 
		  connectionstyle='angle3')
mp.annotate(r'$[\frac{\pi}{2}, 1]$', 
	xycoords='data', xy=(np.pi/2, 1), 
	textcoords='offset points', xytext=(20,-10),
	fontsize=12, arrowprops=ap)

mp.annotate(r'$[\frac{\pi}{2}, 0]$', 
	xycoords='data', xy=(np.pi/2, 0), 
	textcoords='offset points', xytext=(-50,-50),
	fontsize=12, arrowprops=ap)


# 显示图例
mp.legend(loc='best')
mp.show()
