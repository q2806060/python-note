"""
demo06_binomial.py 二项分布
"""
import numpy as np

# 某人投篮命中率0.3, 投10次, 进5个的概率.
r = np.random.binomial(10, 0.3, 100000)
p = (r==5).sum() / r.size
print(p)

# 7个好苹果, 3个坏苹果, 抽出3个苹果, 
# 求抽出2个好苹果的概率
r = np.random.hypergeometric(7, 3, 3, 100000)
p = (r==2).sum() / r.size
print(p)



