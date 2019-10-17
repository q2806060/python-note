"""
demo06_p.py 应用题
"""
import numpy as np

prices = np.mat('3 3.2; 3.5 3.6')
totals = np.mat('118.4; 135.2')
x = np.linalg.lstsq(prices, totals)[0]
print(x)

x = prices.I * totals
print(x)

A = np.mat('1 -2 1; 0 2 -8; -4 5 9')
B = np.mat('0; 8; -9')
print(np.linalg.solve(A, B))

m = np.mat('1 1; 1 0')
for i in range(1, 30):
	print((m**i)[0,1], end=' ')


