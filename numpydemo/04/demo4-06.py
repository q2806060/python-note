import numpy as np 



ary = np.random.uniform(0, 10, (3, 5))
ary = ary.astype(int)
print(ary)

def func(data):
    print(data)
    return data.mean()

r = np.apply_along_axis(func, 0, ary)
print(r)