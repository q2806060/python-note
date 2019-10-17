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
