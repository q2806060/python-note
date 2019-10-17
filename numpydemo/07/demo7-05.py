import numpy as np 


# r = np.random.binomial(10, 0.3, 100000)
# p = (r==5).sum() / r.size
# print(p)

r = np.random.hypergeometric(7,3,3,10)
print(r)