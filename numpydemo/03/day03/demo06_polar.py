"""
demo06_polar.py  极坐标系
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(0, 8*np.pi, 1000)
y = 0.6 * x

mp.figure('Polar', facecolor='lightgray')
mp.title('Polar', fontsize=16)
mp.grid(linestyle=':')
mp.gca(projection='polar')
mp.plot(x, y, color='dodgerblue')
mp.show()