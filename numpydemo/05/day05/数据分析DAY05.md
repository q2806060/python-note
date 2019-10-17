# 数据分析DAY05

### 线性预测

假设一组数据符合一种线性规律, 那么就可以预测未来将会出现的数据.

```
a  b  c  d  e  f  g  h  ....
ax + by + cz = d
bx + cy + dz = e
cx + dy + ez = f
```

基于矩阵求解三元一次方程组:
$$
\left[ \begin{array}{c}
a & b & c \\
b & c & d \\
c & d & e \\
\end{array} \right]
\times
\left[ \begin{array}{c}
x\\
y\\
z\\
\end{array} \right]
=
\left[ \begin{array}{c}
d\\
e\\
f\\
\end{array} \right]
\\
\quad A \quad\quad\quad\quad\quad\quad\quad\quad   B
$$
np提供了相关API求解上述方程:

```python
x = np.linalg.lstsq(A, B)
```

案例: 假设收盘价符合线性规律, 基于线性预测, 预测下一天的收盘价.

```python
"""
demo01_lpred.py  线性预测
"""
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

# 当numpy解析文本时,将会把第一列中的每个字符串
# 都传给函数进行处理, 将处理完毕后的返回值
# 转成需要的M8[D]类型
def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')
	# 把dmy转成日期对象
	d = dt.datetime.strptime(dmy, '%d-%m-%Y')
	t = d.date()
	s = t.strftime('%Y-%m-%d')
	return s

# 加载文件
dates, closing_prices = np.loadtxt(
	'../da_data/aapl.csv', delimiter=',', 
	usecols=(1,6), unpack=True, 
	dtype='M8[D], f8' , 
	converters={1:dmy2ymd})

# 绘制收盘价
mp.figure('Linear Predict', facecolor='lightgray')
mp.title('Linear Predict', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 设置主刻度定位器为每周一
ax = mp.gca()
ax.xaxis.set_major_locator(
	md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(
	md.DateFormatter('%Y/%m/%d'))

# 把M8[D]转为matplotlib识别的date类型
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, 
	color='dodgerblue', linewidth=1,
	linestyle='--', label='closing_prices')

# 整理三元一次方程组, 基于线性模型, 实现线性预测
N = 5

pred_vals = np.zeros(closing_prices.size-2*N+1)

for i in range(pred_vals.size):
	A = np.zeros((N, N))
	for j in range(N):
		A[j,] = closing_prices[j+i:i+j+N]
	B = closing_prices[i+N:i+N*2]
	x = np.linalg.lstsq(A, B)[0]
	pred = B.dot(x) # B点乘x  [3]*x + [4]*y + [5]*z
	pred_vals[i] = pred

# 绘制预测折线图
mp.plot(dates[2*N:], pred_vals[:-1], 'o-',
	color='red', label='Predict Prices')

mp.legend()
# 自动格式化x轴的日期输出
mp.gcf().autofmt_xdate()
mp.show()
```

### 线性拟合

线性拟合可以寻求与一组数据走向趋势规律相适应的线性表达式方程.

有一组股价:

```
[x1, y1]
[x2, y2]
[x3, y3]
...
[xn, yn]
```

根据y = kx+b:

```
y1 = kx1 + b
y2 = kx2 + b
y3 = kx3 + b
....
yn = kxn + b
```

$$
\left[ \begin{array}{c}
x1 & 1\\
x2 & 1\\
x3 & 1\\
xn & 1\\
\end{array} \right]
\times
\left[ \begin{array}{c}
k\\
b\\
\end{array} \right]
=
\left[ \begin{array}{c}
y1\\
y2\\
y3\\
yn\\
\end{array} \right]
$$

使用np.linalg.lstsq(A, B) 求得的x与b, 可能无法让所有的方程成立, 但是拟合的直线方程的误差是最小的.

案例: 利用线性拟合画出股价的趋势线.

 趋势线: (最高价+最低价+收盘价) / 3

```python
"""
demo02_lstsq.py  线性拟合  拟合股价趋势线
"""
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

# 当numpy解析文本时,将会把第一列中的每个字符串
# 都传给函数进行处理, 将处理完毕后的返回值
# 转成需要的M8[D]类型
def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')
	# 把dmy转成日期对象
	d = dt.datetime.strptime(dmy, '%d-%m-%Y')
	t = d.date()
	s = t.strftime('%Y-%m-%d')
	return s

# 加载文件
dates, highest_prices, lowest_prices, \
	closing_prices = np.loadtxt(
	'../da_data/aapl.csv', delimiter=',', 
	usecols=(1,4,5,6), unpack=True, 
	dtype='M8[D], f8, f8, f8' , 
	converters={1:dmy2ymd})

# 绘制收盘价
mp.figure('Linear Predict', facecolor='lightgray')
mp.title('Linear Predict', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 设置主刻度定位器为每周一
ax = mp.gca()
ax.xaxis.set_major_locator(
	md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(
	md.DateFormatter('%Y/%m/%d'))

# 把M8[D]转为matplotlib识别的date类型
dates = dates.astype(md.datetime.datetime)
# 计算所有的趋势点
trend_points = \
	(closing_prices + highest_prices + \
		lowest_prices) / 3

mp.plot(dates, trend_points, 
	color='dodgerblue', linewidth=1,
	linestyle='--', label='closing_prices')

# 线性拟合 lstsq(A, B)  
days = dates.astype('M8[D]').astype(int)
A = np.column_stack((days, np.ones(days.size)))
B = trend_points
x = np.linalg.lstsq(A, B)[0]
# x[0]即是k    x[1]即是b
# 绘制趋势线
trend_line = days*x[0] + x[1]
mp.plot(dates, trend_line, color='orangered',
	label='TrendLine', linewidth=2)

mp.legend()
# 自动格式化x轴的日期输出
mp.gcf().autofmt_xdate()
mp.show()
```

### 协方差、相关矩阵、相关系数

通过两组统计数据计算而得的协方差可以评估这两组统计数据的相似程度.

样本:

```
A = [a1, a2, a3 ... an]
B = [b1, b2, b3 ... bn]
```

求均值:

```
ave_A = np.mean(A)
ave_B = np.mean(B)
```

求离差:

```
dev_A = [a1, a2, a3 .. an] - ave_A
dev_B = [b1, b2, b3 .. bn] - ave_B
```

协方差:

```
cov_ab = np.mean(dev_A * dev_B)
cov_ba = np.mean(dev_B * dev_A)
```

协方差可以简单的反应两组统计样本的相关性. 协方差值为正, 则为正相关; 若值为负, 则为负相关. 绝对值越大相关性越强.

案例: 统计两只股票的相关程度. vale.csv   bhp.csv

```python
# 计算两组数据的协方差
vale_mean = np.mean(vale_closing_prices)
bhp_mean = np.mean(bhp_closing_prices)
dev_vale = vale_closing_prices - vale_mean
dev_bhp = bhp_closing_prices - bhp_mean
cov = np.mean(dev_vale * dev_bhp)
print(cov)
```

**相关系数**

相关系数是一个[-1, 1]之间的数. 若相关系数越接近于1, 则表示两组样本越正相关. 若相关系数越接近于-1, 则表示两组样本越负相关. 若相关系数越接近于0, 则表示两组样本没啥大关系.

相关系数的计算方式 (协方差除以两组样本标准差之积):

```
cov_ab / (std_a * std_b)  a对于b的相关系数
cov_ba / (std_b * std_a)  b对于a的相关系数
```

案例:

```python
# 计算两支股票的相关系数
k = cov / (np.std(vale_closing_prices) * \
			np.std(bhp_closing_prices))
print('K:', k)
```

**相关矩阵**

```python
# 获取相关矩阵, 该矩阵中包含相关系数
# 所以,当需要获取两组数据的相关系数时,
# 可以通过该矩阵得到相关系数的值.
m = np.corrcoef(vale_prices, bhp_prices)
```

$$
\left[ \begin{array}{c}
1 & 0.86\\
0.86 & 1\\
\end{array} \right]   
\quad\quad
\left[ \begin{array}{c}
a与a的相关系数 & a与b的相关系数\\
b与a的相关系数 & b与b的相关系数\\
\end{array} \right]   
$$

```python
# 获取相关矩阵的分子矩阵 (协方差矩阵)
cm = np.cov(a, b)
```

### 多项式拟合

多项式的一般形式:
$$
y = p_0x^n+p_1x^{n-1}+p_2x^{n-2}+...+p_n
$$
多项式拟合的目的是为了找到一组p<sub>0</sub>-p<sub>n</sub> , 使得拟合方程尽可能的与实际样本数据相符合.

假设拟合得到的多项式函数如下:
$$
f(x) = p_0x^n+p_1x^{n-1}+p_2x^{n-2}+...+p_n
$$
拟合得到的多项式函数与真实结果的误差方如下:
$$
loss=(y_1-f(x_1))^2 + (y_2-f(x_2))^2 + ...(y_n-f(x_n))^2  
$$
那么多项式拟合的过程即为求取一组p<sub>0</sub>-p<sub>n</sub> , 使得loss的值最小.

多项式操作相关的API:

```python
# 多项式拟合
# x, y:    为一组样本数据
# 最高次幂: 想得到的多项式函数的最高次幂  4
# p: 返回拟合得到的多项式的系数数组
p = np.polyfit(x,  y, 最高次幂) 
# 把x带入多项式函数p, 求得每个x对应的函数值
_y = np.polyval(p, x)
# 多项式求导  返回导函数的系数数组Q
Q = np.polyder(p)
# 已知多项式系数p, 求多项式函数的根(y=0时x的值)
xs = np.roots(p)

# 求两个多项式函数的差函数 (P1, P2)
Q = np.polysub(P1, P2)
```

案例:求多项式 y=4x<sup>3</sup> + 3x<sup>2</sup> -1000x + 1 曲线的驻点坐标.

```python
"""
demo04_poly.py 多项式函数
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-20, 20, 1000)
y = 4*x**3 + 3*x**2 -1000*x + 1

# 求驻点坐标
P = np.array([4, 3, -1000, 1])
Q = np.polyder(P)
xs = np.roots(Q)
ys = np.polyval(P, xs)

mp.plot(x, y, color='dodgerblue')
mp.scatter(xs, ys, s=60, marker='s', c='red',
	zorder=3)
mp.show()
```

案例: 拟合bhp与vale的差价数据.

```python

# 使用多项式拟合diff曲线
days = dates.astype('M8[D]').astype(int)
P = np.polyfit(days, diff, 4)
_y = np.polyval(P, days)
mp.plot(dates, _y, c='orangered', 
	linewidth=2, label='Polyfit Line')
```

### 数据平滑

数据的平滑处理通常包含有降噪/拟合等操作.降噪的功能在于去除额外的影响因素. 拟合的目的在于数据的数学模型化, 可以通过更多的数学工具识别曲线特征.

案例: 绘制两只股票的收益率曲线. 

收益率=(后一天收盘价-前一天收盘价) / 前一天收盘价

```python
"""
demo06_ph.py  数据平滑处理
"""
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

# 当numpy解析文本时,将会把第一列中的每个字符串
# 都传给函数进行处理, 将处理完毕后的返回值
# 转成需要的M8[D]类型
def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')
	# 把dmy转成日期对象
	d = dt.datetime.strptime(dmy, '%d-%m-%Y')
	t = d.date()
	s = t.strftime('%Y-%m-%d')
	return s

# 加载文件
dates, vale_closing_prices = np.loadtxt(
	'../da_data/vale.csv', delimiter=',', 
	usecols=(1,6), unpack=True, 
	dtype='M8[D], f8' , 
	converters={1:dmy2ymd})

bhp_closing_prices = np.loadtxt(
	'../da_data/bhp.csv', delimiter=',', 
	usecols=(6,), unpack=True)


# 绘制收盘价
mp.figure('Profit', facecolor='lightgray')
mp.title('Profit', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 设置主刻度定位器为每周一
ax = mp.gca()
ax.xaxis.set_major_locator(
	md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(
	md.DateFormatter('%Y/%m/%d'))

# 把M8[D]转为matplotlib识别的date类型
dates = dates.astype(md.datetime.datetime)

# 整理两只股票的收益率
bhp_returns = np.diff(
	bhp_closing_prices) / bhp_closing_prices[:-1]
vale_returns = np.diff(
	vale_closing_prices) / vale_closing_prices[:-1]
dates = dates[:-1]

mp.plot(dates, bhp_returns, c='dodgerblue',
	label='bhp_returns',linewidth=1,
	alpha=0.5)
mp.plot(dates, vale_returns, c='orangered',
	label='vale_returns',linewidth=1,
	alpha=0.5)

# 卷积降噪
core = np.hanning(8)
core /= core.sum()
bhp_returns_convolved = \
	np.convolve(bhp_returns, core, 'valid')
vale_returns_convolved = \
	np.convolve(vale_returns, core, 'valid')
print(bhp_returns_convolved.size)

mp.plot(dates[7:], bhp_returns_convolved,
	c='dodgerblue', linewidth=2,
	label='bhp_convolved')
mp.plot(dates[7:], vale_returns_convolved,
	c='orangered', linewidth=2,
	label='vale_convolved')


mp.legend()
# 自动格式化x轴的日期输出
mp.gcf().autofmt_xdate()
mp.show()

```



















