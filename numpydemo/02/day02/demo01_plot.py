"""
demo01_plot.py  基本绘图API
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1, 7, 2, 4, 8, 2])
mp.plot(x, y)
# 绘制水平垂直线
mp.vlines(4, 1, 8)
mp.hlines(5, 1, 6)
mp.show()



