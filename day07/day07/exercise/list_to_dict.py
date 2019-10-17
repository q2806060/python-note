#   2. 已知有两个等长度的列表list1和lists2, 生成相应字典
#     list1 = [1001, 1002, 1005, 1008]
#     list2 = ['Tom', 'Jerry', 'Spike', 'Tyke']
#     生成的字典为:
#     {'Tom':1001, 'Jerry': 1002, ....}


list1 = [1001, 1002, 1005, 1008]
list2 = ['Tom', 'Jerry', 'Spike', 'Tyke']

# d = {x : y for x in list2 for y in list1} 错误做法
# 方法1
# d = {list2[i]: list1[i] for i in range(len(list1))}

# 方法2
d = {k: list1[list2.index(k)]  for k in list2}



print(d)