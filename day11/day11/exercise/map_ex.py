#   1. 求 1**2 + 2**2 + 3**2 + ..... + 9**2的和
#   2. 求 1**3 + 2**3 + 3**3 + ..... + 9**3的和
#   3. 求 1**9 + 2**8 + 3**7 + ..... + 9**1的和


# 1. 求 1**2 + 2**2 + 3**2 + ..... + 9**2的和
# 方法1
# s = 0
# for x in range(1, 10):
#     s += x ** 2
# print("第一个和为:", s)

# 方法2
s = 0
def pow2(x):
    return x**2
for x in map(pow2, range(1, 10)):
    s += x
print("第一个和为:", s)
# 方法3
s = 0
for x in map(lambda y:y**2, range(1, 10)):
    s += x
print("第一个和为:", s)
# 方法4
print("第一个和为:",
      sum(map(lambda x:x**2, range(1, 10)))
      )

# 2. 求 1**3 + 2**3 + 3**3 + ..... + 9**3的和
print("第二个和为:",
      sum(map(lambda x:x**3, range(1, 10)))
      )
# 3. 求 1**9 + 2**8 + 3**7 + ..... + 9**1的和
print("第三个和为:",
      sum(map(lambda x, y:x**y, range(1, 10),
              range(9, 0, -1)))
      )
print("第三个和为:",
      sum(map(pow, range(1, 10), range(9, 0, -1)))
      )
