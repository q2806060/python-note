"""
demo09_bld.py  布林带
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
mp.plot(dates, closing_prices, alpha=0.8, 
	color='dodgerblue', linewidth=2,
	linestyle='--', label='closing_prices')

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

mp.legend()
# 自动格式化x轴的日期输出
mp.gcf().autofmt_xdate()
mp.show()
