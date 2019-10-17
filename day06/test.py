# import copy

# l1 = [1, 2, [3.1, 3.2]]
# l2 = l1  # 1.不拷贝  L2 和 L1同时绑定同一个对象
# l3 = l1.copy()  # 浅拷贝

# l4 = copy.deepcopy(l1)

# l4[0] = 0
# print(l4)
# print(l1)
# l4[2][1] = 0
# print(l4)
# print(l1)

t = (1, 2, 3) + (4, 5, 6)
print(t)