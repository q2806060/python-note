import numpy as np 
import matplotlib.pyplot as mp 


n = 500 

x = np.random.normal(172, 20, n)

y = np.random.normal(65, 10, n)

mp.figure("Persons", facecolor="lightgray")
mp.title("Person Points", fontsize=16)
mp.xlabel("Height", fontsize=12)
mp.ylabel("Weight", fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
d = (x-172)**2 + (y-65)**2
mp.scatter(x, y, c=d, cmap="jet", alpha=0.6, label="Person")
mp.legend()
mp.show()