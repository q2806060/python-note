# 数据分析DAY04

### 加载文件

#### 绘制K线图

```python
"""
demo01_k.py  k线图
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

# 绘制收盘价
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=18)
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
mp.plot(dates, closing_prices, alpha=0.3,
	color='dodgerblue', linewidth=2,
	linestyle='--', label='closing_prices')

# 绘制K线图 
# 研究颜色的设置
rise = closing_prices >= opening_prices
# 填充色:
color = np.array([('white' if x else 'green') \
		for x in rise])
# 边缘色:
ecolor = np.array([('red' if x else 'green') \
		for x in rise])

# 绘制影线
# mp.bar(dates, highest_prices-lowest_prices, 
# 	0.1, lowest_prices, color=ecolor)
mp.vlines(dates, lowest_prices, highest_prices,
	color=ecolor, linewidth=0.8)
# 绘制实体
mp.bar(dates, closing_prices-opening_prices, 
	0.8, opening_prices, color=color, 
	edgecolor=ecolor, zorder=3)

mp.legend()
# 自动格式化x轴的日期输出
mp.gcf().autofmt_xdate()
mp.show()
```

#### 算数平均值

算数平均值表示对真值的无偏估计.

```
S = [s1, s2, s3 .... sn]
m = (s1+s2+s3+ .... +sn) / n
```

```python
# 求array数组的均值
np.mean(array)
```

案例: 绘制30日收盘价的均线.

```python
# 绘制均线
mean = np.mean(closing_prices)
mp.hlines(mean, dates[0], dates[-1], 
	color='orangered', label='Mean(ClosingP)')
```

#### 加权平均值

```
S = [s1, s2, s3 ... sn]  # 样本
W = [w1, w2, w3 ... wn]  # 权重
A = (s1w1 + s2w2 + ... snwn)/(w1+w2+..wn)
```

```python
# 计算加权平均值
# closing_prices: 样本数组
# weights: 权重数组
np.average(closing_prices, weights=array)
```

**成交量加权平均值**  (VWAP)

以每天的交易量作为权重, 计算加权平均值. (VWAP体现了市场对当前交易价格的认可度)

```python
# 成交量加权均线
vwap = np.average(closing_prices, weights=volumns)
mp.hlines(vwap, dates[0], dates[-1], 
	color='limegreen', label='VWAP')
```

**时间加权平均值** (TWAP)

```python
# 时间加权均线
times = np.arange(1, closing_prices.size+1)
twap = np.average(closing_prices, weights=times)
mp.hlines(twap, dates[0], dates[-1], 
	color='violet', label='TWAP')
```

#### 最值

```python
np.max(array)  # 求array数组的最大值
np.min(array)  # 求array数组的最小值
np.pip(array)  # 求array数组的极差(max-min)
```

```python
np.argmax(array)	# 获取array数组最大值的下标
np.argmin(array)	# 获取array数组最小值的下标
```

```python
# a与b是同维数组
# 留下两数组中相比的最大值组成新数组
np.maximum(a, b)	
# 留下两数组中相比的最小值组成新数组
np.minimum(a, b)
```

案例:

```python
"""
demo03_max.py  极值
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

# 评估AAPL股票的最高价与最低价的波动性 
max_price = np.max(highest_prices)
min_price = np.min(lowest_prices)
print(max_price, min_price)

# 查看最高价与最低价到底是哪一天
max_i = np.argmax(highest_prices)
min_i = np.argmin(lowest_prices)
print(dates[max_i], dates[min_i])

a = np.arange(1, 10)
b = a[::-1]
a = a.reshape(3, 3)
b = b.reshape(3, 3)
print(np.maximum(a, b))
print(np.minimum(a, b))
```

#### 中位数

将多个样本按照大小排序, 取中间位置的元素.

```python
# 对有序数组array 求中位数
m = np.median(ary)
# 中位数算法
m = (ary[(size-1)/2] + ary[size/2]) / 2
```

案例:

```python
# 绘制中位数水平线
sorted_prices = np.msort(closing_prices)
median = np.median(sorted_prices)
# 自己计算
size = sorted_prices.size
median = (sorted_prices[int((size-1)/2)] + \
		sorted_prices[int(size/2)]) / 2
print(median)
mp.hlines(median, dates[0], dates[-1], 
	color='gold', label='Median')
```

**当样本集中没有太多异常数据时可以用平均数. 如果有一些异常数据(极大/极小), 比较适合使用中位数.**

#### 标准差

标准差用于衡量一组数据的离散程度.

```
样本:  S=[s1, s2, s3 ... sn]
均值:  m = np.mean(s)
离差:  D = [d1, d2, d3 .. dn]  (di=si-m)
离差方: Q = [q1, q2, q3 .. qn]  (qi=di^2) 
总体方差:  v=Q的均值  (q1+q2+q3 .. qn)/n
总体标准差: s = sqrt(v)  

样本方差:  v'=Q的均值  (q1+q2+q3 .. qn)/(n-1)
样本标准差: s' = sqrt(v')  
```

标准差相关API:

```python
# 总体标准差
std = np.std(array)
# 样本标准差   ddof为修正参数 意味着分母:n-1
std = np.std(array, ddof=1)
```

案例:

```python
# 获取收盘价的标准差
print(np.std(closing_prices))
print(closing_prices.std())
print(np.std(closing_prices, ddof=1))

# 自己算标准差
mean = np.mean(closing_prices)
d = closing_prices - mean
d2 = d ** 2
var = np.mean(d2)
std = np.sqrt(var)
print(std)
```

### 案例应用

#### 时间数据处理

案例: 统计每个周一/周二/...周五的收盘价的均值, 并输出.

```python
"""
demo06_dp.py  
统计每个周一/周二/...周五的收盘价的均值, 并输出.
"""
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

# 当numpy解析文本时,将会把第一列中的每个字符串
# 都传给函数进行处理, 将处理完毕后的返回值
# 转成需要的int类型  (0 1 2 3 4 5 6)
def dmy2weekday(dmy):
	dmy = str(dmy, encoding='utf-8')
	# 把dmy转成日期对象
	d = dt.datetime.strptime(dmy, '%d-%m-%Y')
	t = d.date()
	wday = t.weekday()
	return wday

# 加载文件
dates, closing_prices = np.loadtxt(
	'../da_data/aapl.csv', delimiter=',', 
	usecols=(1,6), unpack=True, 
	dtype='f8, f8', 
	converters={1:dmy2weekday})

print(dates)
# 存储最终结果 [周一均价, 周二均价....]
ave_closing_prices = np.zeros(5)
for wday in range(ave_closing_prices.size):
	ave_closing_prices[wday] = \
		closing_prices[dates==wday].mean()

print(np.round(ave_closing_prices, 2))
```

#### 数组的轴向汇总

轴向汇总相关API:

```python
def func(data):
    pass
# func 轴向汇总函数名
# axis 轴向  0 1
# array 原数组
np.apply_along_axis(func, axis, array)
```

案例:

```python
"""
demo07_aaa.py  测试数组轴向汇总相关API
"""
import numpy as np

ary = np.random.uniform(0, 10, (3, 5))
ary = ary.astype(int)
print(ary)
# 轴向汇总
def func(data):
	print('--',data)
	return data.mean(), data.max(), data.min()

r = np.apply_along_axis(func, 0, ary)
print(r)
```

#### 移动平均线

绘制5日移动均线: 从第五天开始,每天计算最近5天的收盘价的平均值而构成的一条线.

移动均线算法:

```
a b c d e f g h ...
s1 = (a+b+c+d+e)/5
s2 = (b+c+d+e+f)/5
s3 = (c+d+e+f+g)/5
....
[s1, s2, s3 ...] 这组数据构成的一条线称为移动均线
```

案例: 绘制5日移动平均线

```python
# 计算5日均线
sma5 = np.zeros(closing_prices.size - 4)
for i in range(sma5.size):
	sma5[i] = closing_prices[i:i+5].mean()
mp.plot(dates[4:], sma5, color='orangered',
	label='SMA-5', linewidth=2)
```

#### 卷积运算

卷积运算的过程:

```
原数组: [1 2 3 4 5]
卷积核数组: [8 7 6]
使用卷积核对原数组执行卷积运算的过程如下:

	       44 65 86       - 有效卷积(valid)
        23 44 65 86 59    - 同维卷积(same)
      8 23 44 65 86 59 30 - 完全卷积(full)
0  0  1  2  3  4  5  0  0
6  7  8
   6  7  8
      6  7  8
         6  7  8
            6  7  8
               6  7  8
                  6  7  8
```

卷积运算相关API:

```python
# array: 原数组
# core:  卷积核数组
# type: 卷积类型
#    'valid': 有效卷积
#    'same':  同维卷积
#    'full':  完全卷积
r = np.convolve(array, core, type)
```

案例: 使用卷积实现5日均线.

```python
# 基于卷积实现5日均线
core = np.ones(5) / 5
sma52 = np.convolve(closing_prices, core, 'valid')
mp.plot(dates[4:], sma52, color='orangered',
	label='SMA-52', alpha=0.3, linewidth=7)

# 使用卷积绘制10日均线
core = np.ones(10) / 10
sma10 = np.convolve(closing_prices, core, 'valid')
mp.plot(dates[9:], sma10, color='limegreen',
	label='SMA-10', linewidth=3)
```

**加权卷积运算**

```python
# 实现加权5日均线
# 从y=e^x, 取得5个函数值作为卷积核.
weights = np.exp(np.linspace(-1, 0 ,5))
weights = weights[::-1]
weights /= weights.sum()
ema5 = np.convolve(closing_prices, weights, 'valid')
mp.plot(dates[4:], ema5, color='red',
	label='EMA5', linewidth=2)
```

卷积常用于数据平滑处理/降噪等操作. 可以更好的看出数据的走势. 需要考虑清楚的是卷积核的选取. 

#### 布林带

布林带由3条线组成:

中轨: 移动平均线

上轨: 中轨+2*5日收盘价标准差

下轨: 中轨-2*5日收盘价标准差

案例:

```python

# 实现加权5日均线
# 从y=e^x, 取得5个函数值作为卷积核.
weights = np.exp(np.linspace(-1, 0 ,5))
weights = weights[::-1]
weights /= weights.sum()
ema5 = np.convolve(closing_prices, weights, 'valid')
mp.plot(dates[4:], ema5, color='red',
	label='EMA5', linewidth=2, alpha=0.5)

# 绘制布林带
stds = np.zeros(ema5.size)
for i in range(stds.size):
	stds[i] = closing_prices[i:i+5].std()

# 计算上轨与下轨
uppers = ema5+2*stds
lowers = ema5-2*stds
mp.plot(dates[4:], uppers, color='red',
	label='Uppers', linewidth=2, alpha=0.5)
mp.plot(dates[4:], lowers, color='red',
	label='Lowers', linewidth=2, alpha=0.5)
mp.fill_between(dates[4:], uppers, lowers, 
	uppers>lowers, color='red', alpha=0.3)
```







