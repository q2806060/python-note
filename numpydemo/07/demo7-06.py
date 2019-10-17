import numpy as np 



p = np.array(['苹果','华为','OPPO','MI','VIVO'])
prices = [8888, 4500, 3999, 2999, 3999]
totals = np.array([100, 200, 99, 110, 80])

indices = np.lexsort((totals*-1, prices))

