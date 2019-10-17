import numpy as np 
import matplotlib.pyplot as mp 
import datetime as dt
import matplotlib.dates as md

# 当numpy解析文本时，将会把第一行中的每个字符串都传给函数进行处理，将处理完毕后的返回值转成需要的M8[D]类型
def dmy2ymd(dmy):
    dmy = str(dmy, encoding="utf-8")
    d = dt.datetime.strptime(dmy, '%d-%m-%Y')
    t = d.date()
    s = t.strftime('%Y-%m-%d')
    return s 

dates, closing_prices = np.loadtxt(
    'C:/Users/Administrator/Desktop/sucai/da_data/aapl.csv',
    delimiter=",",
    usecols=(1,6),
    unpack=True,
    dtype="M8[D], f8",
    converters={1:dmy2ymd}
)

# 绘制收盘价
mp.figure("AAPL", facecolor="lightgray")
mp.title("APPL", fontsize=18)
mp.xlabel("Date", fontsize=14)
mp.ylabel("Price", fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")

# 设置主刻度定位器为每周一
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter('%Y/%m/%d'))

# 把M8[D]转换为matplotlib识别的date类型
dates = dates.astype(md.datetime.datetime)

mp.plot(dates, closing_prices, color="dodgerblue", linewidth=3, linestyle="--", label="closing_prices")
mp.legend()
# 自动格式化x轴的日期输出
mp.gcf().autofmt_xdate()
mp.show()