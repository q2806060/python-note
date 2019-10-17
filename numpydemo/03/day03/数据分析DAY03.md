# 数据分析DAY03

#### 区域填充

以某种颜色填充两条曲线的闭合区域.

```python
mp.fill_between(
	x, 				# x值的区间
    sin_x, 			# 与x组成一条曲线
    cos_x, 			# 与x组成第二条曲线
    sin_x < cos_x,	# 绘制填充的条件
    color='',		
    alpha=0.5
)
```

案例: 绘制 sin_x=sin(x)    cos_x=cos(x/2)/2     [0, 8π]

```python
"""
demo01_fill.py   区域填充
"""
import numpy as np
import matplotlib.pyplot as mp

n = 1000
x = np.linspace(0, 8*np.pi, n)
sin_x = np.sin(x)
cos_x = np.cos(x/2) / 2 

mp.figure('Fill', facecolor='lightgray')
mp.title('Fill', fontsize=16)
mp.xlabel('X', fontsize=12)
mp.ylabel('Y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, sin_x, color='dodgerblue',
	label=r'$y=sin(x)$')
mp.plot(x, cos_x, color='orangered',
	label=r'$y=\frac{1}{2}cos(\frac{x}{2})$')
mp.fill_between(
    x, sin_x, cos_x, 
    sin_x>cos_x,
	color='deepskyblue', alpha=0.6)
mp.fill_between(
    x, sin_x, cos_x, 
    sin_x<cos_x,
	color='orangered', alpha=0.6)
mp.legend()
mp.show()
```

#### 条形图(柱状图)

```python
mp.bar(
    x, 			# 横坐标数组
    height, 	# 对应每个x的柱子的高度
    width,		# 对应每个x的柱子的宽度
    color='',   
    label='',
    alpha=0.2
)
```

案例:

```python
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
```

#### 饼状图

```python
mp.pie(
	values, 		# 扇形值列表
    spaces,			# 扇形之间间距列表
    labels,         # 扇形标签文本列表
    colors,			# 扇形颜色列表
    '%.2f%%',		# 百分比的格式
    shadow=True,	# 阴影
    startangle=90,	# 饼状图的绘制起始角度
    radius=1		# 饼状图的半径
)
```

案例:

```python
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
```

#### 等高线图

等高线图属于3D数学模型, 需要整理网格点坐标矩阵, 还需要得到每个点的高度值.

等高线相关API:

```python
# 绘制等高线
cntr = mp.contour(
	x, y,	# x,y为二维数组,组成网格点坐标矩阵
    z, 		# 每个坐标的高度值
    8,		# 把整体高度分为8份
    colors='',	# 等高线的颜色
    linewidths=''	# 等高线的线宽
)
# cntr等高线对象绘制标注
mp.clabel(cntr, 
          inline_spacing=1, # 文本与线的间隔
          fmt='%.1f',fontsize=10) 
# 等高线填充颜色
mp.contourf(x, y, z, 8, cmap='jet')
```

案例:

```python
"""
demo04_contour.py  等高线图
"""
import numpy as np
import matplotlib.pyplot as mp

# 生成网格点坐标矩阵
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
				   np.linspace(-3, 3, n))
# 根据x,y 计算当前坐标下的z高度值
z = (1-x/2 + x**5 + y**3) * np.exp(-x**2 -y**2)

mp.figure('Contour', facecolor='lightgray')
mp.title('Contour', fontsize=18)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
cntr = mp.contour(x, y, z, colors='black', 
		   linewidths=0.5)
# cntr等高线对象绘制标注
mp.clabel(cntr, inline_spacing=1, fmt='%.1f',
	      fontsize=10)
# 等高线填充颜色
mp.contourf(x, y, z, 8, cmap='jet')

mp.show()
```

#### 热成像图

```python
# 以jet映射显示z矩阵的图像值
# origin: y坐标轴方向
#  lower: 较小的数字在下方
#  upper: 较小的数字在上方
mp.imshow(z, cmap='jet', origin='lower')
```

案例:

```python
"""
demo05_imshow.py  热成像图
"""
import numpy as np
import matplotlib.pyplot as mp

# 生成网格点坐标矩阵
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
				   np.linspace(-3, 3, n))
# 根据x,y 计算当前坐标下的z高度值
z = (1-x/2 + x**5 + y**3) * np.exp(-x**2 -y**2)

mp.figure('Imshow', facecolor='lightgray')
mp.title('Imshow', fontsize=18)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.imshow(z, cmap='jet', origin='lower')
mp.show()
```

#### 极坐标系

当需要处理角度相关的函数图像时, 可能需要使用极坐标系绘制图像.

```python
mp.gca(projection='polar')
mp.plot()
```

案例: r = 0.6 * t     &theta; 关于 &rho; 的函数

```python
"""
demo06_polar.py  极坐标系
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(0, 8*np.pi, 1000)
y = 0.6 * x

mp.figure('Polar', facecolor='lightgray')
mp.title('Polar', fontsize=16)
mp.grid(linestyle=':')
mp.gca(projection='polar')
mp.plot(x, y, color='dodgerblue')
mp.show()
```

#### 3D图像的绘制

matplotlib支持绘制三维线框图, 三维曲面图, 三维散点图. 需要使用axes3d提供3d坐标系.

```python
from mpl_toolkits.mplot3d import axes3d
ax3d = mp.gca(projection='3d')

ax3d.plot_wireframe()	# 绘制3d线框图
ax3d.plot_surface()		# 绘制3d曲面图
ax3d.scatter()			# 绘制3d散点图
```

**三维线框图**

```python
ax3d.plot_wireframe(
    x, y, 	# x,y网格点坐标矩阵
    z, 		# z为每个坐标点的值
	rstride=30,	# 行跨距
    cstride=30, # 列跨距
    linewidth=1,
    color=''
)	
```

案例:

```python
"""
demo06_wireframe.py  三维线框图
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

# 生成网格点坐标矩阵
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
				   np.linspace(-3, 3, n))
# 根据x,y 计算当前坐标下的z高度值
z = (1-x/2 + x**5 + y**3) * np.exp(-x**2 -y**2)

mp.figure('Wireframe', facecolor='lightgray')
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('X', fontsize=14)
ax3d.set_ylabel('Y', fontsize=14)
ax3d.set_zlabel('Z', fontsize=14)
ax3d.plot_wireframe(x, y, z, rstride=10, 
	cstride=10,color='dodgerblue')
mp.show()
```

**三维曲面图**

```python
ax3d.plot_surface(
    x, y, 	# x,y网格点坐标矩阵
    z, 		# z为每个坐标点的值
	rstride=30,	# 行跨距
    cstride=30, # 列跨距
    cmap='jet'
)	
```

**三维散点图**

```python
ax3d.scatter(
	x, y, z,  		 # x,y,z  确定一组散点坐标
    marker='',		 # 点型
    s = 60,			 # 点的大小
    edgecolor='',	 # 边缘色
    facecolor='',	 # 填充色
    zorder=3,		 # 绘制图层编号 
    c=d,			 # 设置过渡性颜色
    cmap='jet'		 # 颜色映射
)
```

#### 简单动画

动画即是在一段时间内快速连续的重新绘制图像的过程.

matplotlib提供了方法用于处理简单动画的绘制:

```python
import matplotlib.animation as ma
def update(number):
    pass

# 每隔30毫秒,执行一次update
ma.FuncAnimation(
    mp.gcf(),   # 作用域当前窗体
    update,     # 更新函数的函数名
    interval=30 # 每隔30毫秒,执行一次update
)  
```

案例: 随机生成各种颜色的100个气泡, 让他们不断增大.

1. 随机生成100个气泡.
2. 每个气泡拥有四个属性: position, size, growth, color
3. 把每个气泡绘制到窗口中.
4. 开启动画,在update函数中更新每个气泡的属性并重新绘制

```python
"""
demo11_bubble.py  简单动画
1. 随机生成100个气泡.
2. 每个气泡拥有四个属性: position, size, growth, color
3. 把每个气泡绘制到窗口中.
4. 开启动画,在update函数中更新每个气泡的属性并重新绘制
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

n = 100
balls = np.zeros(n, dtype=[
		('position', float, 2), # 位置属性
		('size', float, 1),     # 大小属性
		('growth', float, 1),   # 生长速度
		('color', float, 4)])   # 颜色属性
# 初始化每个泡泡
# uniform: 从0到1取随机数,填充n行2列的数组
balls['position']=np.random.uniform(0,1,(n,2))
balls['size']=np.random.uniform(50,70,n)
balls['growth']=np.random.uniform(10,20,n)
balls['color']=np.random.uniform(0,1,(n,4))
# 绘制100个泡泡
mp.figure('Bubble', facecolor='lightgray')
mp.title('Bubble', fontsize=18)
mp.xticks([])
mp.yticks([])
sc = mp.scatter(balls['position'][:,0], 
	       balls['position'][:,1],
	       balls['size'], 
	       color=balls['color'])

# 启动动画
def update(number):
	balls['size'] += balls['growth']
	# 让某个泡泡破裂,从头开始执行
	boom_i = number % n
	balls[boom_i]['size'] = 60
	balls[boom_i]['position']= \
			np.random.uniform(0, 1, (1, 2))
	# 重新设置属性
	sc.set_sizes(balls['size'])
	sc.set_offsets(balls['position'])

anim = ma.FuncAnimation(
	mp.gcf(), update, interval=30)

mp.show()
```

基于生成器函数提供数据, 实现动画的绘制.

```python
def update(data):
    pass

def generator():
    yield data 
    
# 每10毫秒执行生成器, 把结果交给update, 更新图像
ma.FuncAnimation(
    mp.gcf(), 
    update, 	# 更新函数
    generator,  # 生成器函数
	interval=10
)
```

案例: 模拟心电图.  y = sin(2πt)*exp(sin(0.2πt))

```python
"""
demo12_gen.py  模拟心电图
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

mp.figure('Signal', facecolor='lightgray')
mp.title('Signal', fontsize=16)
mp.xlim(0, 10)
mp.ylim(-3, 3)
mp.grid(linestyle=':')
pl = mp.plot([],[], color='dodgerblue',
		label='Signal')[0]
# 启动动画
def update(data):
	t, v = data
	x, y = pl.get_data()  #x y: ndarray数组
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
	y = np.sin(2 * np.pi * x) * \
		np.exp(np.sin(0.2 * np.pi * x))
	yield (x, y)
	x += 0.05

anim = ma.FuncAnimation(mp.gcf(), 
	update, generator, interval=30)
mp.show()
```

### numpy常用函数

#### 加载文件

```python
dates, opening_prices = np.loadtxt(
	'../xxxx/aapl.csv',	# 文件路径
    delimiter=',',		# 分隔符
    unpack=True,		# 是否拆包
    usecols=(1,3),		# 需要读取哪些列
    dtype='U10, f8',	# 设置每列的数据类型
    converters={1:func} # 数据转换器
)
```

案例:

```python

```















