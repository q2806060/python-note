import numpy as np 
import matplotlib.pyplot as mp 
import matplotlib.animation as ma 

n = 100
balls = np.zeros(n, dtype=[
    ("position", float, 2),
    ("size", float, 1),
    ("growth", float, 1),
    ("color", float, 4)
])
# 初始化每个泡泡
# uniform:从0到1取随机数，填充n行2列的数组
balls['position'] = np.random.uniform(0, 1,(n, 2))
balls['size'] = np.random.uniform(50, 70,n)
balls['growth'] = np.random.uniform(10, 40, n)
balls['color'] = np.random.uniform(0, 1,(n, 4))

# 绘制100个泡泡
mp.figure("Bubble", facecolor="lightgray")
mp.title("Bubble", fontsize=18)
mp.xticks([])
mp.yticks([])
sc = mp.scatter(balls['position'][:,0],balls['position'][:,1],balls['size'],color=balls['color'])

#启动动画
def update(number):
    balls['size'] += balls['growth']
    # 让某个泡泡破裂，从头开始执行
    boom_i = number % n
    balls[boom_i]['size'] = 60
    balls[boom_i]['position'] = np.random.uniform(0, 1,(1, 2))
    sc.set_sizes(balls['size'])
    sc.set_offsets(balls['position'])

anim = ma.FuncAnimation(mp.gcf(), update, interval=30)

mp.show()