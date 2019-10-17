#    3. 生成前40 个斐波那契数(Fibonacci)
#       1   1   2   3   5   8  13  ...
#       要求，将这些数保存在列表中
#       　最后打印出这些数

# 方法1
# L = [1, 1]
# a = 1
# b = 1
# while len(L) < 40:
#     fibo = a + b
#     L.append(fibo)
#     a = b
#     b = fibo

# 方法2
# L = []
# a = 0
# b = 1  # 当前fibonacci 数
# while len(L) < 40:
#     L.append(b)
#     # 再求下个数fibonacci数
#     a, b = b, a + b

#     # next_fibo = a + b
#     # a = b
#     # b = next_fibo

# 方法3
L = [1, 1]
while len(L) < 40:
    L.append(L[-2] + L[-1])


print(L)



