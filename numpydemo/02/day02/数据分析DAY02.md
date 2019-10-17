# 数据分析DAY02

## matplotlib概述

matplotlib是python的一个绘图库.使用它可以很方便的绘制出版质量级别的图形.

### matplotlib的基本功能

1. 基本绘图
   1. 绘制折线, 设置线型/线宽/颜色等.
   2. 设置坐标轴范围
   3. 设置坐标刻度
   4. 设置坐标轴位置/颜色
   5. 图例
   6. 特殊点
   7. 备注
2. 高级图形操作
   1. 子图
   2. 操作刻度定位器/刻度网格线
   3. 半对数坐标
   4. 散点图
   5. 图像填充
   6. 条形图/饼状图
   7. 等高线图/热成像图
   8. 3D图形
   9. 简单动画
   10. 极坐标系

## matplotlib功能详解

### 基本绘图

#### 绘图核心API

```python
import matplotlib.pyplot as mp
# 把多个点连起来绘制一条折线
# xarray: 所有点的x坐标
# yarray: 所有点的y坐标
mp.plot(xarray, yarray)
mp.show()
```

绘制水平线/垂直线

```python
# 绘制垂直线
mp.vlines(val, ymin, ymax)
# 绘制水平线
mp.hlines(val, xmin, xmax)
```

案例:绘制一条正弦曲线 [-π, π]

```python
"""
demo02_plot.py  绘制一条正弦曲线
"""
import numpy as np
import matplotlib.pyplot as mp

# [-π,π] 拆1000个点
x = np.linspace(-np.pi, np.pi, 1000)
sin_x = np.sin(x)
# 绘制余弦曲线 y=1/2 * cos(x)
cos_x = np.cos(x) / 2
# 绘图
mp.plot(x, sin_x)
mp.plot(x, cos_x)
mp.show()
```

#### 线型、线宽和颜色

```python
# color:
#   英文颜色单词 或 常见颜色单词首字母   
#   #ABC23E
#   (0.5, 0.3, 0.8) 或 (0.5, 0.3, 0.8, 0.4)
mp.plot(
    x, y, 			# 点的坐标数组
	linestyle='',	# 线型:  ':'  '-'  '--'
    linewidth=3,	# 线宽:  3倍线宽
    color='',		# 颜色
    alpha=0.3		# 透明度
)
```

#### 设置坐标轴范围

```python
# 设置x轴的可视范围   [x_min, x_max]
mp.xlim(x_min, x_max)
# 设置y轴的可视范围   [y_min, y_max]
mp.ylim(y_min, y_max)
```

#### 设置坐标刻度

```python
# 设置x轴的坐标刻度
# x_val_list:  x轴刻度值序列
# x_text_list: x轴刻度值的文本序列(可选)
mp.xticks(x_val_list, x_text_list)
# 设置y轴的坐标刻度
# y_val_list:  y轴刻度值序列
# y_text_list: y轴刻度值的文本序列(可选)
mp.yticks(y_val_list, y_text_list)
```

**刻度文本的特殊语法** - latex语法
$$
a^2 + b^2 = c^2 \quad\quad\quad
-\frac{\pi}{2} \quad\quad\quad
\sqrt[3]{\frac{5}{2}}
$$

#### 设置坐标轴

```python
# 获取当前坐标轴
ax = mp.gca()
axis = ax.spines['left']
axis = ax.spines['right']
axis = ax.spines['top']
axis = ax.spines['bottom']
# 修改坐标轴的颜色  
axis.set_color('none')
# 移动坐标轴的位置  
# data: 基于数据坐标系进行定位   0: 把坐标轴移动到0的位置
axis.set_position(('data', 0))
```

案例:

```python
# 设置坐标轴
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
```

#### 图例

```python
# label: 定义当前曲线的标签名 该标签名将会在图例中显示
mp.plot(x, y, label='sin(x)')
# 显示图例  loc:图例的位置  (参照legend()文档字符串)
mp.legend(loc='best')
```

#### 特殊点

```python
mp.scatter(
	xarray, yarray,  # 给出点的坐标
    marker='',		 # 点型  'D'  's'  'o' ...
    s = 60,			 # 点的大小
    edgecolor='',	 # 边缘色
    facecolor='',	 # 填充色
    zorder=3		 # 绘制图层编号 (编号越大,图层越靠上)
)
```

#### 备注

```python
mp.annotate(
	r'$[x, y]$', 		# 备注的文本内容
    xycoords='data',	# 目标点的坐标系
    xy=(1, 2),			# 目标点的坐标
    # 定位备注文本位置所使用的坐标系
    textcoords='offset points',	
    xytext=(-10, -10),	# 备注文本的坐标
    fontsize=12,		# 字体大小
    # 箭头属性字典
    arrowprops=dict(
    	arrowstyle : '->',			# 箭头样式
        connectionstyle='angle3'	# 连接线的样式
    )
)
```

### 高级图形操作

案例：绘制两个窗口，一起显示。

```python
# 手动创建一个窗口,窗口的标题titleA
mp.figure('titleA', facecolor='填充色')
# 手动创建第二个窗口,窗口的标题titleB
mp.figure('titleB', facecolor='填充色')
# 由于titleA已经创建过,将会把titleA窗口置为当前窗口
mp.figure('titleA')
mp.show()
```

**设置当前窗口的常用参数**

```python
# 设置图表的标题
mp.title(' ', fontsize=12)
# 设置水平轴的标签
mp.xlabel('time', fontsize=12)
# 设置垂直轴的标签
mp.ylabel('v', fontsize=12)
# 设置刻度参数
mp.tick_params(labelsize=8)
# 设置图表网格线
mp.grid(linestyle=':')
# 紧凑布局
mp.tight_layout()
```

#### 子图

子图可以在一个窗口中显示多张图表.

**矩阵式布局**

矩阵式布局相关API:

```python

```

案例:

```python
mp.figure('Subplot A', facecolor='lightgray')

for i in range(9):
	mp.subplot(3,3,i+1)
	mp.xticks([])
	mp.yticks([])
	mp.text(0.5, 0.5, i+1, ha='center', 
		    va='center', size=36, alpha=0.5)
	mp.tight_layout()
mp.show()
```

**网格式布局**

网格式布局支持单元格的合并.

```python
import matplotlib.gridspec as mg
mp.figure(...)
# 构建3*3的网格布局结构
gs = mg.GridSpec(3, 3)
mp.subplot(gs[0, :2])
mp.show()
```

案例:

```python
"""
demo05_subplot.py 网格式布局
"""
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

mp.figure('Grid Layout', facecolor='lightgray')
gs = mg.GridSpec(3, 3)

mp.subplot(gs[0, :2])
mp.text(0.5, 0.5, '1', ha='center',
	    va='center', size=36)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[:2, 2])
mp.text(0.5, 0.5, '2', ha='center',
	    va='center', size=36)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[1, 1])
mp.text(0.5, 0.5, '3', ha='center',
	    va='center', size=36)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[1:, 0])
mp.text(0.5, 0.5, '4', ha='center',
	    va='center', size=36)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[2, 1:])
mp.text(0.5, 0.5, '5', ha='center',
	    va='center', size=36)
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.show()
```

**自由布局**

```python
mp.figure()
# 0.1, 0.2: 子图左下角定点坐标
# 0.5: 子图的宽度   0.3:子图的高度
mp.axes([0.1, 0.2, 0.5, 0.3])
mp.text(...)
mp.show()
```

#### 刻度定位器

```python
# 获取当前坐标轴
ax = mp.gca()
# 设置x轴的主刻度定位器
locator1 = mp.NullLocator()
ax.xaxis.set_major_locator(locator1)
# 设置x轴的次刻度定位器
locator2 = mp.MultipleLocator(0.1)
ax.xaxis.set_minor_locator(locator2)
```

案例: 绘制一个数轴.

```python
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
```

#### 刻度网格线

```python
ax = mp.gca()
ax.grid(
	which='', # 'major'|'minor'|'both'
    axis='',  # 'x'|'y'|'both'
    linewidth=1,
    linestyle=':',
    color='',
    alpha=0.5
)
```

案例:

```python
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
```

#### 半对数坐标

y轴将会以指数方式递增. 基于半对数坐标系表示上述曲线可以更好的观察底部数据细节.

```python
# plot改为semilogy, 坐标系将会改为半对数坐标系
mp.semilogy()
```

#### 散点图

| 身高 | 体重 | 性别 | 年龄 | 民族 |
| ---- | ---- | ---- | ---- | ---- |
| 180  | 75   | 0    | 18   | 0    |
| 175  | 60   | 1    | 20   | 1    |

绘制散点图相关API:

```python
mp.scatter(
	xarray, yarray,  # 给出点的坐标
    marker='',		 # 点型
    s = 60,			 # 点的大小
    edgecolor='',	 # 边缘色
    facecolor='',	 # 填充色
    zorder=3,		 # 绘制图层编号 
    c=d,			 # 设置过渡性颜色
    cmap='jet'		 # 颜色映射
)
```

随机生成符合 正态分布 的随机数:

```python
n = 500
# 随机生成n个数
# 172: 数学期望
# 20:  标准差
x = np.random.normal(172, 20, n)
```









