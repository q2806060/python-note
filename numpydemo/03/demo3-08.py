import numpy as np 
import matplotlib.pyplot as mp 
import mpl_toolkits.mplot3d as axes3d

n = 1000
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)
d = np.sqrt(x**2 + y**2 + z**2)
mp.figure("3D Scatter")
ax3d = mp.gca(projection="3d")
ax3d.set_xlabel("X", fontsize=14)
ax3d.set_ylabel("Y", fontsize=14)
ax3d.set_zlabel("Z", fontsize=14)
ax3d.scatter(x, y, z, s=60, alpha=0.6, c=d, cmap='jet')
mp.show()