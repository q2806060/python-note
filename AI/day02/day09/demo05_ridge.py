"""
demo05_ridge.py  岭回归
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
import sklearn.metrics as sm

x ,y = np.loadtxt('../ml_data/abnormal.txt', 
	delimiter=',', usecols=(0,1), 
	unpack=True)
# 把x改为n行1列  这样才可以作为输入交给模型训练
x = x.reshape(-1, 1)
mp.figure('Ridge Regression', facecolor='lightgray')
mp.title('Ridge Regression', fontsize=18)
mp.xlabel('X', fontsize=16)
mp.ylabel('Y', fontsize=16)
mp.tick_params(labelsize=12)
mp.grid(linestyle=':')
mp.scatter(x, y, s=60, c='dodgerblue', 
	label='Points')

# 使用线性回归, 绘制回归线
model = lm.LinearRegression()
model.fit(x, y)
pred_y = model.predict(x)
mp.plot(x, pred_y, c='orangered', 
		label='Linear Regression Line')

# 使用岭回归, 绘制回归线
model = lm.Ridge(150, fit_intercept=True, 
	    max_iter=1000)
model.fit(x, y)
pred_y = model.predict(x)
mp.plot(x, pred_y, c='limegreen', 
		label='Ridge Regression Line')


mp.legend()
mp.show()