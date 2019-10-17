"""
demo10_anim.py  简单动画
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

def update(number):
	print(number)

mp.figure('Animation')
# 启动动画, 每30毫秒执行一次update函数
anim = ma.FuncAnimation(
	mp.gcf(), update, interval=1000)
mp.show()