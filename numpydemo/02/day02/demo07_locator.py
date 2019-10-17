"""
demo07_locator.py 刻度定位器
"""
import matplotlib.pyplot as mp

locators = ['mp.NullLocator()', 
			'mp.MultipleLocator(2)', 
			'mp.MaxNLocator(nbins=6)',
			'mp.AutoLocator()',
			'mp.FixedLocator(locs=[0, 5, 10])']

mp.figure('Locator', facecolor='lightgray')

for i, locator in enumerate(locators):
	mp.subplot(len(locators), 1, i+1)
	ax = mp.gca()
	ax.spines['left'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.spines['right'].set_color('none')
	mp.ylim(-1, 1)
	mp.xlim(0, 10)
	mp.yticks([])
	ax.spines['bottom'].set_position(('data', 0))
	# 设置水平轴的刻度定位器
	ax.xaxis.set_major_locator(eval(locator))

	l2 = mp.MultipleLocator(0.1)
	ax.xaxis.set_minor_locator(l2)


mp.show()
