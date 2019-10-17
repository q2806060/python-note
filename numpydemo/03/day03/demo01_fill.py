"""
demo01_fill.py   区域填充
"""
import numpy as np
import matplotlib.pyplot as mp

n = 1000
x = np.linspace(0, 8*np.pi, n)
sin_x = np.sin(x)
cos_x = np.cos(x/2) / 2 

mp.figure('Fill', facecolor='lightgray')
mp.title('Fill', fontsize=16)
mp.xlabel('X', fontsize=12)
mp.ylabel('Y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, sin_x, color='dodgerblue',
	label=r'$y=sin(x)$')
mp.plot(x, cos_x, color='orangered',
	label=r'$y=\frac{1}{2}cos(\frac{x}{2})$')
mp.fill_between(x, sin_x, cos_x, sin_x>cos_x,
	color='deepskyblue', alpha=0.6)
mp.fill_between(x, sin_x, cos_x, sin_x<cos_x,
	color='orangered', alpha=0.6)
mp.legend()
mp.show()


