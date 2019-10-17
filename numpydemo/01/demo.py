import numpy as np

# demo1
# ary = np.array([1,2,3,4])
# print(ary)
# print(type(ary))
# ary = ary + 10
# print(ary)

# demo2创建一个两行四列的数组
a = np.array(
    [
    [1,2,3,4],
    [5,6,7,8]
    ]
)
print(a, a.shape)

# demo3创建9个元素的数组
b = np.arange(1, 10, 1)
print(b, b.shape)

# demo4创建10个元素为0的数组
c = np.zeros(10)
print(c, c.dtype)

# demo5创建5个元素全为1的数组
d = np.ones(5, dtype="int32")
print(d)

# demo6 创建与a结构类型相同的数组，数值全为0及1
e = np.zeros_like(a)
f = np.ones_like(a)
print(e)
print(f)