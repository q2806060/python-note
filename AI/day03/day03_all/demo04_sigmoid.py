import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-50, 50, 1000)
y = 1 / (1+np.exp(-x))

mp.grid(linestyle=':')
mp.plot(x, y)
mp.show()