"""
demo02_bike.py  共享单车案例   随机森林
"""
import numpy as np
import sklearn.utils as su
import sklearn.ensemble as se
import sklearn.metrics as sm
import matplotlib.pyplot as mp

data = np.loadtxt('../ml_data/bike_day.csv', 
	delimiter=',', unpack=False, 
	dtype='U20')
# 获取输入集与输出集
header = data[0, 2:13]
x = np.array(data[1:, 2:13], dtype=float)
y = np.array(data[1:, -1], dtype=float)
# 打乱数据集
x, y = su.shuffle(x, y, random_state=7)
# 拆分训练集,测试集
train_size = int(len(x)*0.9)
train_x, test_x, train_y, test_y = \
	x[:train_size], x[train_size:], \
	y[:train_size], y[train_size:]
# 随机森林模型训练
model=se.RandomForestRegressor(max_depth=10, 
	n_estimators=1000, min_samples_split=2)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
# 使用r2得分验证预测结果
print(sm.r2_score(test_y, pred_test_y))
# 输出特征重要性
fi_day = model.feature_importances_
print(fi_day)
print(header)

# 绘制特征重要性柱状图
mp.figure('Bike', facecolor='lightgray')
mp.subplot(211)
mp.title('Day', fontsize=16)
mp.ylabel('Importances', fontsize=12)
mp.tick_params(labelsize=8)
mp.grid(linestyle=':')
pos = np.arange(fi_day.size)
sorted_i = fi_day.argsort()[::-1]
mp.xticks(pos, header[sorted_i])
mp.bar(pos, fi_day[sorted_i], 
	   color='dodgerblue', label='Bike_Day')
mp.legend()


data = np.loadtxt('../ml_data/bike_hour.csv', 
	delimiter=',', unpack=False, 
	dtype='U20')
# 获取输入集与输出集
header = data[0, 2:14]
x = np.array(data[1:, 2:14], dtype=float)
y = np.array(data[1:, -1], dtype=float)
# 打乱数据集
x, y = su.shuffle(x, y, random_state=7)
# 拆分训练集,测试集
train_size = int(len(x)*0.9)
train_x, test_x, train_y, test_y = \
	x[:train_size], x[train_size:], \
	y[:train_size], y[train_size:]
# 随机森林模型训练
model=se.RandomForestRegressor(max_depth=10, 
	n_estimators=1000, min_samples_split=2)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
# 使用r2得分验证预测结果
print(sm.r2_score(test_y, pred_test_y))
# 输出特征重要性
fi_hour = model.feature_importances_
print(fi_hour)
print(header)

mp.subplot(212)
mp.title('Hour', fontsize=16)
mp.ylabel('Importances', fontsize=12)
mp.tick_params(labelsize=8)
mp.grid(linestyle=':')
pos = np.arange(fi_hour.size)
sorted_i = fi_hour.argsort()[::-1]
mp.xticks(pos, header[sorted_i])
mp.bar(pos, fi_hour[sorted_i], 
	   color='orangered', label='Bike Hour')
mp.legend()
mp.show()



















