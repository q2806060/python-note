"""
demo02_mean.py  绘制均线
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
mp.plot(dates, closing_prices, alpha=0.6,
	color='dodgerblue', linewidth=2,
	linestyle='--', label='closing_prices')

# 绘制均线
mean = np.mean(closing_prices)
mp.hlines(mean, dates[0], dates[-1], 
	color='orangered', label='Mean(ClosingP)')

# 成交量加权均线
vwap = np.average(closing_prices, weights=volumns)
mp.hlines(vwap, dates[0], dates[-1], 
	color='limegreen', label='VWAP')

# 时间加权均线
times = np.arange(1, closing_prices.size+1)
twap = np.average(closing_prices, weights=times)
mp.hlines(twap, dates[0], dates[-1], 
	color='violet', label='TWAP')


mp.legend()
# 自动格式化x轴的日期输出
mp.gcf().autofmt_xdate()
mp.show()
