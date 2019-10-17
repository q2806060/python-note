"""
demo02_bar.py 柱状图
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.arange(12)
apples=[98,12,37,65,18,94,56,23,49,56,24,56]
oranges=[75,20,39,65,23,65,10,23,94,76,89,12]

mp.figure('Bar Chart', facecolor='lightgray')
mp.title('Bar Chart', fontsize=16)
mp.xlabel('Month', fontsize=14)
mp.ylabel('Num', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.bar(x+0.2, apples, 0.4, color='limegreen',
	   label='Apples')
mp.bar(x-0.2, oranges, 0.4, color='orangered',
	   label='Oranges')
# 设置刻度
mp.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr',
	'May', 'Jun', 'Jul', 'Aug', 'Sep',
	'Oct', 'Nov', 'Dec'])

mp.legend()
mp.show()
