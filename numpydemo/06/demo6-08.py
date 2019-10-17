import numpy as np 
import matplotlib.pyplot as mp 


x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.zeros(x.size)

y1 = 4*np.pi*np.sin(x)
y2 = 4/3*np.pi * np.sin(3*x)
y3 = 4/5*np.pi * np.sin(5*x)
y = y1 + y2 + y3 

y = np.zeros(x.size)
for i in range(1,10):
    y += 4/(2*i-1)*np.pi * np.sin((2*i-1)*x)


mp.grid(linestyle=":")
mp.plot(x, y, color="dodgerblue", linewidth=2)
mp.show()
