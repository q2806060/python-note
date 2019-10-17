import numpy as np 

a = np.array([50, 60, 80, 45, 30])
b = np.piecewise(a, [a<60, a==60, a>60], [-1, 0, 1])
print(b)