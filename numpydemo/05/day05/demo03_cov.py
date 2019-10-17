"""
demo03_cov.py  协方差示例
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
mp.figure('COV DEMO', facecolor='lightgray')
mp.title('COV DEMO', fontsize=18)
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
mp.plot(dates, vale_closing_prices, 
	color='dodgerblue', linewidth=1,
	linestyle='--', label='vale prices')
mp.plot(dates, bhp_closing_prices, 
	color='orangered', linewidth=1,
	linestyle='--', label='bhp prices')

# 计算两组数据的协方差
vale_mean = np.mean(vale_closing_prices)
bhp_mean = np.mean(bhp_closing_prices)
dev_vale = vale_closing_prices - vale_mean
dev_bhp = bhp_closing_prices - bhp_mean
cov = np.mean(dev_vale * dev_bhp)
print('COV:', cov)

# 计算两支股票的相关系数
k = cov / (np.std(vale_closing_prices) * \
			np.std(bhp_closing_prices))
print('K:', k)

# 相关矩阵
m = np.corrcoef(vale_closing_prices, 
				bhp_closing_prices)
print(m)
print(np.cov(vale_closing_prices, bhp_closing_prices))

mp.legend()
# 自动格式化x轴的日期输出
mp.gcf().autofmt_xdate()
mp.show()
