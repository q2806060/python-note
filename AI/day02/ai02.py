import sklearn.datasets as sd 
import sklearn.utils as su


# 读取数据 加载波士顿房屋价格
boston = sd.load_boston()
print(boston.data.shape)        # 数据的维度
print(boston.feature_names)     # 数据的特征名

# 划分测试集与训练集
# 打乱数据集，以random_state随机种子作为参数生成数据集
x, y = su.shuffle(boston.data, boston.target, random_state=7)
train_size = len(x)


