import numpy as np 
import sklearn.preprocessing as sp 

samples = np.array([
    [17, 100, 4000],
    [20, 80, 5000],
    [23, 70, 5500]])

r = sp.normalize(samples, norm='l1')
print(r)