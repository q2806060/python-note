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

dates, hightest_prices, lowest_prices, closing_prices = np.loadtxt(
    'C:/Users/Administrator/Desktop/sucai/da_data/aapl.csv',
    delimiter=",",
    usecols=(1,4,5,6),
    unpack=True,
    dtype="M8[D], f8,f8,f8",
    converters={1:dmy2ymd}
)

# 绘制收盘价
mp.figure("Linear Predict", facecolor="lightgray")
mp.title("Linear Predict", fontsize=18)
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

# 计算所有的趋势点
trend_points = (closing_prices+hightest_prices+lowest_prices)/3

# 线性拟合 lstsq(A, B)  
days = dates.astype('M8[D]').astype(int)
A = np.column_stack((days, np.ones(days.size)))
B = trend_points
x = np.linalg.lstsq(A, B)[0]
# 绘制趋势线
trend_line = days*x[0] + x[1]
mp.plot(dates, trend_line, color='orangered', label='Trendline', linewidth=2)


mp.plot(dates, closing_prices, color="dodgerblue", linewidth=1, linestyle="--", label="closing_prices")


# # 整理三元一次方程组，基于线型模型，实现线型预测
# N = 3

# pred_vals = np.zeros(closing_prices.size-2*N+1)

# for i in range(pred_vals.size):
#     A = np.zeros((N, N))
#     for j in range(N):
#         A[j, ] = closing_prices[j+i:i+j+N]
#     B = closing_prices[i+N:i+N*2]
#     x = np.linalg.lstsq(A, B)[0]
#     pred = B.dot(x)     # B点乘x
#     pred_vals[i] = pred

# # 绘制预测折线图
# mp.plot(dates[2*N:], pred_vals[:-1], "o-", color="red", label="Predict Prices")

mp.legend()
# 自动格式化x轴的日期输出
mp.gcf().autofmt_xdate()
mp.show()