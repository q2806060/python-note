import numpy as np 
import matplotlib.pyplot as mp 
import matplotlib.animation as ma 

mp.figure("Signal", facecolor="lightgray")
mp.title("Signal", fontsize=16)
mp.xlim(0, 10)
mp.ylim(-3, 3)
mp.grid(linestyle=":")
pl = mp.plot([],[],color='dodgerblue', label="Signal")[0]

# 启动动画
def update(data):
    t, v = data
    x, y = pl.get_data()    # x, y: ndarray数组
    x = np.append(x, t)
    y = np.append(y, v)
    # 重新绘制图像
    pl.set_data(x, y)
    # 移动坐标轴
    if x[-1]>5:
        mp.xlim(x[-1]-5, x[-1]+5)

x = 0
def generator():
    global x 
    y = np.sin(2**np.pi*x) * np.exp(np.sin(0.2*np.pi*x))
    yield (x, y)
    x += 0.05


anim = ma.FuncAnimation(mp.gcf(), update, generator, interval=30)
mp.show()