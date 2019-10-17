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
# 使用piecewise替代sign函数
sign_prices = np.piecewise(diff_prices, 
	[diff_prices<0, diff_prices==0, diff_prices>0],
	[-1, 0, 1])

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
