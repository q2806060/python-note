"""
demo04_poly.py 多项式函数
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-20, 20, 1000)
y = 4*x**3 + 3*x**2 -1000*x + 1

# 求驻点坐标
P = np.array([4, 3, -1000, 1])
Q = np.polyder(P)
xs = np.roots(Q)
ys = np.polyval(P, xs)

mp.plot(x, y, color='dodgerblue')
mp.scatter(xs, ys, s=60, marker='s', c='red',
	zorder=3)
mp.show()
