import numpy as np 
import matplotlib.pyplot as mp 

x = np.arange(1, 13)
apples = [53,51,61,31,45,15,34,35,15,15,14,35]
oranges = [87,35,73,62,86,73,26,59,26,87,23,65]

mp.figure("Bar Chart", facecolor="lightgray")
mp.title("Bar Chart", fontsize=16)
mp.xlabel("Month", fontsize=14)
mp.ylabel("Num", fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.bar(x+0.2, apples, 0.4, color="limegreen", label="Apples")
mp.bar(x-0.2, oranges, 0.4, color="orangered", label="Ornages")
mp.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
mp.legend()
mp.show()