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