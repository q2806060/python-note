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
