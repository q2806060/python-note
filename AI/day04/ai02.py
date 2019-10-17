import numpy as np 
import sklearn.preprocessing as sp 
import sklearn.ensemble as se 
import sklearn.model_selection as ms 

data = np.loadtxt('C:\\Users\\Administrator\\Desktop\\sucai\\ml_data\\car.txt', dtype='U20', delimiter=',')

data = data.T 
encoders = []
train_x, train_y = [], []

for row in range(len(data)):
    # 创建适用于当前特征的标签编码器
    encoder = sp.LabelEncoder()
    if row < len(data) - 1:
        train_x.append(encoder.fit_transform(data[row]))
    else:
        train_y = (encoder.fit_transform(data[row]))
    
    encoders.append(encoder)

train_x = np.array(train_x).T
train_y = np.array(train_y)

# 模型训练
model = se.RandomForestClassifier(max_depth=6, n_estimators=200, random_state=7)
# 交叉验证
# score = ms.cross_val_score(model, train_x, train_y, cv=4, scoring='f1_weighted')
# print(score)

# 输出验证曲线，选取最优的n_estimators
train_scores, test_scores = ms.validation_curve(model, train_x, train_y, 'n_estimators', np.arange(50, 500, 50), cv=5)

print(train_scores, test_scores)


# model.fit(train_x, train_y)
