"""
demo06_polyfit.py  多项式回归
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
import sklearn.metrics as sm
import sklearn.preprocessing as sp
import sklearn.pipeline as pl

x ,y = np.loadtxt('../ml_data/single.txt', 
	delimiter=',', usecols=(0,1), 
	unpack=True)
# 把x改为n行1列  这样才可以作为输入交给模型训练
x = x.reshape(-1, 1)
# 训练多项式回归模型
model = pl.make_pipeline(
	sp.PolynomialFeatures(10), 
	lm.LinearRegression()
)
model.fit(x, y)
pred_y = model.predict(x)
# 为了绘制多项式模型曲线, 构建1000个点
test_x = np.linspace(x.min(), x.max(), 1000)
test_x = test_x.reshape(-1, 1)
pred_test_y = model.predict(test_x)


# 评估回归模型的误差
# 平均绝对值误差  1/m∑|预测输出-真实输出|
print(sm.mean_absolute_error(y, pred_y))
# 平均平方误差  sqrt(1/m∑(预测输出-真实输出)^2)
print(sm.mean_squared_error(y, pred_y))
# 中位数绝对值误差  median(|预测输出-真实输出|)
print(sm.median_absolute_error(y, pred_y))
# r2得分 (0,1]的一个分值,分数越高,误差越小
print(sm.r2_score(y, pred_y))

mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=18)
mp.xlabel('X', fontsize=16)
mp.ylabel('Y', fontsize=16)
mp.tick_params(labelsize=12)
mp.grid(linestyle=':')
mp.scatter(x, y, s=60, c='dodgerblue', 
	label='Points')
mp.plot(test_x, pred_test_y, c='orangered', 
	linewidth=2, label='Regression Line')
mp.legend()
mp.show()