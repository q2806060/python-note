"""
demo07_house.py  预测房屋价格
"""
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.metrics as sm


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
model=st.DecisionTreeRegressor(max_depth=6)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))


