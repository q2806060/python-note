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
