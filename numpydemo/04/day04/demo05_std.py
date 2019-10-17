"""
demo05_std.py  标准差
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