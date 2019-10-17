import numpy as np 
import matplotlib.pyplot as mp 

# 数据预处理
# 加载数据
x = np.array([[1,0], [0,0], [0,1], [1,1], [1,1]])
y = np.array([[0], [0], [0], [1], [1]])

# 数据可视化
for _x, _y in zip(x,y):
    mp.plot(_x[0], _x[1], 'o' if _y[0] else '^', c='r' if _y[0] else 'b')

# mp.show()

# 权重参数
w = np.random.normal(0, 0.01, size=[2,1])

b = np.random.normal(0, 0.01, size=[1])

# 预测输出
output = np.dot(x, w) + b 

print(output)