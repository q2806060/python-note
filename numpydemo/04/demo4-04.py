import numpy as np 
import matplotlib.pyplot as mp 
import datetime as dt
import matplotlib.dates as md

# 当numpy解析文本时，将会把第一行中的每个字符串都传给函数进行处理，将处理完毕后的返回值转成需要的M8[D]类型
def dmy2weekday(dmy):
    dmy = str(dmy, encoding="utf-8")
    d = dt.datetime.strptime(dmy, '%d-%m-%Y')
    t = d.date()
    wday = t.weekday()
    return wday

dates, closing_prices = np.loadtxt(
    'C:/Users/Administrator/Desktop/sucai/da_data/aapl.csv',
    delimiter=",",
    usecols=(1,6),
    unpack=True,
    dtype="M8, f8",
    converters={1:dmy2weekday}
)

# 评估AAPL股票的最高价与最低价的波动性
# max_price = np.max(hightest_prices)
# min_price = np.min(lowest_prices)

# max_i = np.argmax(hightest_prices)
# min_i = np.argmin(lowest_prices)

# print(np.std(closing_prices))
# print(np.std(closing_prices, ddof=1))

print(dates)