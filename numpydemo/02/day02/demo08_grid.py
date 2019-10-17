"""
demo08_grid.py  刻度网格线
"""
import matplotlib.pyplot as mp

mp.figure('Grid Line', facecolor='lightgray')
mp.title('Grid Line', fontsize=16)
mp.xlabel('X', fontsize=12)
mp.ylabel('Y', fontsize=12)
mp.tick_params(labelsize=10)
# 绘制刻度网格线
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator())
ax.xaxis.set_minor_locator(
		mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(
		mp.MultipleLocator(250))
ax.yaxis.set_minor_locator(
		mp.MultipleLocator(50))
ax.grid(which='major', axis='both', 
	    linewidth=0.75, linestyle='-', 
	    color='orange')
ax.grid(which='minor', axis='both', 
	    linewidth=0.25, linestyle='-', 
	    color='orange')

y = [1, 10, 100, 1000, 100, 10, 1]
mp.plot(y, color='dodgerblue')
mp.show()
