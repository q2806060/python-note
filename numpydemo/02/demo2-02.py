import numpy as np 
import matplotlib.pyplot as mp 


mp.figure('titleA', facecolor='lightgray')
mp.figure('titleB', facecolor='black')
mp.figure('titleA')
mp.title('sudo', fontsize=12)
# 设置水平轴的标签
mp.xlabel('time', fontsize=12)
# 设置垂直轴的标签
mp.ylabel('v', fontsize=12)
# 设置刻度参数
mp.tick_params(labelsize=10)
# 设置图标网格线
mp.grid(linestyle=":")
# 紧凑布局
mp.tight_layout()
mp.show()