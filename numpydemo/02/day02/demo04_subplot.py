"""
demo04_subplot.py  绘制子图
"""
import matplotlib.pyplot as mp

mp.figure('Subplot A', facecolor='lightgray')

for i in range(9):
	mp.subplot(3,3,i+1)
	mp.xticks([])
	mp.yticks([])
	mp.text(0.5, 0.5, i+1, ha='center', 
		    va='center', size=36, alpha=0.5)
	mp.tight_layout()
mp.show()