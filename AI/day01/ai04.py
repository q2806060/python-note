import numpy as np 
import sklearn.preprocessing as sp


samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 70., 5500]])


# 构建独热编码器
ohe = sp.OneHotEncoder(sparse=False)
r = ohe.fit_transform(samples)
print(r)