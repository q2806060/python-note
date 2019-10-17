import numpy as np 
import matplotlib.pyplot as mp


x = np.linspace(-np.pi, np.pi, 1000)
y = np.sin(x)
mp.plot(x, y, label=r'$y=sin(x)$')

x = np.linspace(-np.pi, np.pi, 1000)
y = np.cos(x)/2
mp.plot(x, y, linestyle="--", color="y",linewidth='3', label=r"$y=\frac{1}{2}cos(x)$")
# mp.xlim(0, np.pi)
# mp.ylim(0,1)
x_val_list = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]
x_text_list = ['-π', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', 'π']
y_val_list = [-1, -0.5, 0.5, 1]
y_text_list = ['-1', '-0.5', '0.5', '1']
mp.xticks(x_val_list, x_text_list)
mp.yticks(y_val_list, y_text_list)

# 获取当前坐标轴
ax = mp.gca()
ax.spines['left'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
mp.legend(loc="upper right")
mp.show()