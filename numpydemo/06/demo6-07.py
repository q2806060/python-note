import numpy as np 



a = np.arange(1, 10)
# print(a.clip(min=3, max=6))
# print(a.compress(a>=6))



a = a.reshape(3, 3)
b = a[::]
print(np.add(a, b))
print(np.add.reduce(a))
print(np.add.accumulate(a))
print(np.add.outer([10, 20], a))
