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
