"""
demo01_adaboost.py  正向激励
"""
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.ensemble as se
import sklearn.metrics as sm
import matplotlib.pyplot as mp
import numpy as np

# 读取数据  加载波士顿房屋价格
boston = sd.load_boston()
print(boston.data.shape)	# 数据的维度
print(boston.feature_names) # 数据的特征名
print(boston.target.shape)

# 划分测试集与训练集
# 打乱数据集 
# 以random_state随机种子作为参数生成数据集
x, y=su.shuffle(boston.data, boston.target, 
				random_state=7)
train_size = int(len(x)*0.8)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], \
    y[:train_size], y[train_size:]

# 创建决策树回归器模型,使用训练集训练模型, 
# 测试集测试模型
t_model=st.DecisionTreeRegressor(max_depth=4)
# 基于正向激励  搞出多颗树
model = se.AdaBoostRegressor(t_model, 
	n_estimators=400, random_state=7)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
fi_ab = model.feature_importances_
print(fi_ab)

# 使用决策树训练模型
model=st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
fi_t = model.feature_importances_


# 绘制特征重要性柱状图
mp.figure('feature_importances',facecolor='lightgray')
mp.subplot(211)
mp.title('feature_importances',fontsize=16)
mp.ylabel('Feature Importances', fontsize=12)
mp.grid(linestyle=':')
sorted_indices = fi_ab.argsort()[::-1]
x = np.arange(fi_ab.size)
mp.xticks(x, boston.feature_names[sorted_indices])
mp.bar(x, fi_ab[sorted_indices], 
	color='dodgerblue', label='fi_ab')
mp.legend()

mp.subplot(212)
mp.title('feature_importances',fontsize=16)
mp.ylabel('Feature Importances', fontsize=12)
mp.grid(linestyle=':')
sorted_indices = fi_t.argsort()[::-1]
x = np.arange(fi_t.size)
mp.xticks(x, boston.feature_names[sorted_indices])
mp.bar(x, fi_t[sorted_indices], 
	color='orangered', label='fi_t')
mp.legend()

mp.show()