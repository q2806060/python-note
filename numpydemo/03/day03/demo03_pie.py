"""
demo03_pie.py  饼状图
"""
import matplotlib.pyplot as mp

mp.figure('Languages', facecolor='lightgray')
mp.title('Languages', fontsize=18)

labels = ['Python', 'Javascript', 'C++', 
          'Java', 'PHP']
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
values = [26, 17, 21, 25, 5]
colors = ['dodgerblue', 'orangered', 
          'limegreen', 'violet', 'gold']

# 等轴比例绘制pie
mp.axis('equal')
mp.pie(values, spaces, labels, colors, 
	   '%.2f%%', shadow=True,
	   startangle=90)
mp.show()

