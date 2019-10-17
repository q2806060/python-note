# 数据分析DAY06

### 符号数组

np.sign()函数可以把样本数组变成对应的符号数组, 正数变为1, 负数变为-1, 0依然为0.

```
a = np.sign(array)
```

**OBV能量潮**

成交量可以反映市场对某支股票的人气. 成交量是一支股票上涨的能量. 股票上涨往往需要较大的成交量. 而下跌时则不然.

若相比上一天收盘价上涨,则为正成交量(红色). 若相比上一天收盘价下跌,则为负成交量(绿色).

案例:

```python
"""
demo01_obv.py  obv能量潮
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
dates, closing_prices, volumns = np.loadtxt(
	'../da_data/aapl.csv', delimiter=',', 
	usecols=(1,6,7), unpack=True, 
	dtype='M8[D], f8, f8' , 
	converters={1:dmy2ymd})

# 绘制OBV
mp.figure('OBV', facecolor='lightgray')
mp.title('OBV', fontsize=18)
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

# 绘制OBV能量潮
diff_prices = np.diff(closing_prices)
sign_prices = np.sign(diff_prices)
up_obvs = volumns[1:][sign_prices>=0]
up_dates = dates[1:][sign_prices>=0]
mp.bar(up_dates, up_obvs, 0.8, 
	   color='red', label='OBV_UP')
down_obvs = volumns[1:][sign_prices==-1]
down_dates = dates[1:][sign_prices==-1]
mp.bar(down_dates, down_obvs, 0.8, 
	   color='green', label='OBV_DOWN')


mp.legend()
# 自动格式化x轴的日期输出
mp.gcf().autofmt_xdate()
mp.show()
```

**数组处理函数**

```python
# 对数组进行二次处理
ary = np.piecewise(源数组, 条件序列, 取值序列)
```

案例:

```python
# 使用piecewise替代sign函数
sign_prices = np.piecewise(
    diff_prices, 
	[diff_prices<0, diff_prices==0, 
     diff_prices>0],
	[-1, 0, 1])
```

### 函数矢量化

函数矢量化: 只能处理标量参数的函数经过函数矢量化后就可以接受数组参数, 对数组中每个元素执行相同处理.

numpy提供了vectorize函数, 可以把普通函数矢量化, 返回矢量化函数, 这样就可以直接处理数组参数.

案例:

```python
"""
demo03_vectorize.py 函数矢量化
"""
import numpy as np
import math as m

def f(a, b):
	r = m.sqrt(a**2 + b**2)
	return r
# 处理标量
print(f(3, 4))
# 处理矢量参数
a = np.array([3, 4, 5])
b = np.array([4, 5, 6])
# 把f函数矢量化
f_vec = np.vectorize(f)
print(f_vec(a, b))
print(np.vectorize(f)(a, b))

# 使用frompyfunc实现函数矢量化
# 2: 函数接收2个参数    1: 函数有1个返回值
f_func = np.frompyfunc(f, 2, 1)
print(f_func(a, b))
```

案例: 定义一种买进卖出策略, 通过历史数据判断这种策略是否可以实施.

```python
"""
demo04_profit.py  自定义投资策略, 求收益
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
dates, opening_prices, highest_prices, \
	lowest_prices, closing_prices = np.loadtxt(
	'../da_data/aapl.csv', delimiter=',', 
	usecols=(1,3,4,5,6), unpack=True, 
	dtype='M8[D], f8, f8, f8, f8', 
	converters={1:dmy2ymd})

# 定义一种投资策略
# 每天开盘价*0.99买入, 收盘价就卖出
def profit(opening_price, highest_price,
		lowest_price, closing_price):
    buying_price = opening_price*0.99
    if lowest_price <= \
        buying_price <= highest_price:
        # 返回收益率的百分比
        return (closing_price-buying_price) * \
		        100 / buying_price
    return np.nan

# 调用函数 求得收益率  
profits = np.vectorize(profit)(opening_prices, 
	highest_prices, lowest_prices, closing_prices)
print(profits)
# 获取nan的掩码数组
nan = np.isnan(profits)
dates, profits = dates[~nan], profits[~nan]

# 绘制收盘价
mp.figure('profits', facecolor='lightgray')
mp.title('profits', fontsize=18)
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
mp.plot(dates, profits, 
	color='dodgerblue', linewidth=2,
	linestyle='-', label='profits')

mp.hlines(profits.mean(), dates[0], 
	dates[-1], color='orangered', 
	linewidth=2)

mp.legend()
# 自动格式化x轴的日期输出
mp.gcf().autofmt_xdate()
mp.show()
```

### 矩阵

矩阵是matrix类型的对象, 该类继承自numpy.ndarray. 任何针对ndarray的操作,对矩阵对象同样有效. 但是作为子类, 矩阵又结合了其自身的特点, 做了必要的扩充. 比如: 矩阵乘法 / 矩阵求逆等运算.

**矩阵对象的创建**

```python
# 构建矩阵对象 
# ary: 任何可以被解释为矩阵的数据结构
# copy: 是否复制数据 (True:复制一份副本数据)
m = np.matrix(ary, copy=True)

np.mat(ary)

np.mat('矩阵拼块规则字符串')
```

**矩阵的乘法运算**

```python
m3 = np.mat('1 2 3; 4 5 6')
print(m3)
print(m3 * 10)
print(m3 * m3.T)
print(m3.T * m3)
```

**矩阵的逆矩阵**

若两个矩阵A / B满足: AB = BA = E (E为单位矩阵). 则称A与B互为逆矩阵. 

单位矩阵E: 主对角线为1, 其他元素都为0.

```python
mi = m.I  
mi = np.linalg.inv(m)
```

矩阵求逆时, 若把方阵推广到非方阵, 则称为矩阵的**广义逆矩阵**.

**矩阵的应用**

假设一帮孩子和家长旅游, 去程坐大巴, 小孩票价3元, 大人票价3.2元, 共花了118.4; 回程坐火车, 小孩票价3.5元, 大人票价3.6元, 共花了135.2. 分别求小孩和大人的人数.

```python
"""
demo06_p.py 应用题
"""
import numpy as np

prices = np.mat('3 3.2; 3.5 3.6')
totals = np.mat('118.4; 135.2')
x = np.linalg.lstsq(prices, totals)[0]
print(x)

x = prices.I * totals
print(x)
```

**解方程组**
$$
\begin{cases}
x-2y+z=0 \\
2y-8z-8=0 \\
-4x+5y+9z+9=0 \\
\end{cases}
$$

```
x = np.linalg.lstsq(A, B)
x = np.linalg.solve(A, B)
```

整理成矩阵相乘的形式:
$$
\left[ \begin{array}{c}
1 & -2 & 1 \\
0 & 2 & -8 \\
-4 & 5 & 9 \\
\end{array} \right]
\times
\left[ \begin{array}{c}
x \\
y \\
z \\
\end{array} \right]
=
\left[ \begin{array}{c}
0 \\
8 \\
-9 \\
\end{array} \right]
$$
案例:

```python
A = np.mat('1 -2 1; 0 2 -8; -4 5 9')
B = np.mat('0; 8; -9')
print(np.linalg.solve(A, B))
```

案例: 求斐波那契数列

1  1   2   3   5    8    13    21   .....

```
x	  1 1   1 1   1 1   
	  1 0   1 0   1 0  
----------------------------------
1 1   2 1   3 2   5 3
1 0   1 1   2 1   3 2  ...
```

案例:

```python
m = np.mat('1 1; 1 0')
for i in range(1, 30):
	print((m**i)[0,1], end=' ')
```

### numpy的通用函数

#### 数组的裁剪与压缩

```python
# 数组的裁剪
ndarray.clip(min=下限, max=上限)
# 数组的压缩
ndarray.compress(条件)
```

```python
a = np.arange(1, 10)
# 数组裁剪: 最小值不小于下限, 最大值不大于上限
print(a.clip(min=3, max=6))
print(a.compress(a>=6))
```

#### 加法通用函数

```python
np.add(a, a)		# 求两数组之和
np.add.reduce(a)	# 求a数组元素的累加和
np.add.accumulate(a)	# 返回a数组累加和的过程
np.add.outer([10, 20, 30], a) # 外和
```

案例:

```python
print('-' * 45)
a = a.reshape(3, 3)
b = a[::]
print(np.add(a, b))
a = a.ravel()
print(a)
print(np.add.reduce(a))  # 求a元素的累加和
print(np.add.accumulate(a)) # a累加和的过程
print(np.add.outer([10,20], a)) # 外和
```

#### 乘除法通用函数

```python
# 返回ndarray数组元素的累乘结果
ndarray.prod()
# 返回ndarray数组元素累乘的过程
ndarray.cumprod()
# a数组 / b数组
np.true_divide(a,b)    np.divide(a,b)
# 地板除
np.floor_divide(a, b)
np.ceil(a / b)   # 天花板取整
np.round(a / b)  # 四舍五入
np.trunc(a / b)  # 截断取整
```

#### 位运算通用函数

**位异或:**

```
c = a ^ b
c = np.bitwise_xor(a, b)
```

按位异或操作可以方便的判断两个数据是否同号.

```
7   0111
6   0110
5   0101
4   0100
3   0011
2   0010
1   0001
0   0000
-1  1111
-2  1110
-3  1101
-4  1100
-5  1011
-6  1010
-7  1001
-8  1000
```

```python
print('-' * 45)
print(a)
print(b)
print(a^b < 0)   # 判断是否异号
print(np.bitwise_xor(a,b) < 0)   # 判断是否异号
```

**位与:**

```python
e = a & b
e = np.bitwise_and(a, b)
```

利用位与运算计算某个数字是否是2的幂.

```
1   2^0   00001        0   00000
2   2^1   00010        1   00001
4   2^2   00100        3   00011
8   2^3   01000        7   00111
16  2^4   10000       15   01111
....
```

案例:

```python
print('-' * 45)
for i in range(1000):
	if i & (i-1) == 0:
		print(i, end=' ')

a = np.arange(1, 1000)
print(a[a&(a-1) == 0])
```

**其他位运算通用函数**

```python
np.bitwise_or(a, b)		# 或运算
np.bitwise_not(a)       # 非
np.left_shift(a, 1)     # 左移
np.right_shift(a, 1)    # 右移
```

#### 三角函数通用函数

```python
np.sin(a)
np.cos(a)
....
```

**傅里叶定理**

法国科学家傅里叶说过, 任何一个周期函数都是n个不同振幅/不同频率/不同相位的正弦函数叠加而成.

**合成方波**

一个方波由如下参数的正弦波叠加而成:
$$
y = 4\pi \times sin(x) \\
y = \frac{4}{3}\pi \times sin(3x) \\
y = \frac{4}{5}\pi \times sin(5x) \\
....\\
y = \frac{4}{2n-1}\pi \times sin((2n-1)x) \\
$$
案例:

```python
"""
demo08_sin.py  叠加方波
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
# 叠加3条曲线
y1 = 4*np.pi * np.sin(x)
y2 = 4/3*np.pi * np.sin(3*x)
y3 = 4/5*np.pi * np.sin(5*x)
y = y1 + y2 + y3
# 叠加1000条曲线
y = np.zeros(x.size)
for i in range(1, 1000):
	y += 4/(2*i-1)*np.pi * np.sin((2*i-1)*x)

mp.grid(linestyle=':')
mp.plot(x, y1)
mp.plot(x, y2)
mp.plot(x, y3)
mp.plot(x, y,linewidth=2)
mp.show()


```

















