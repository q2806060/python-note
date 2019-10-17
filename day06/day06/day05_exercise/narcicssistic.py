#   2. 算出 100 ~ 999 以内的水仙花数(Narcissistic
#       Number)
#     水仙花数是指 百位的3次方 + 十位的3次方 + 个位的3次方
#       等于原数的整数
#     如:
#       153 = 1**3 + 5**3 + 3**3
#     求所有的水仙花数

# 方法1
# for x in range(100, 1000):
#     s = str(x)  # 转为字符串 123--> "123"
#     bai = int(s[0])  # 百位
#     shi = int(s[1])  # 十位
#     ge = int(s[2])  # 个数
#     if x == bai ** 3 + shi ** 3 + ge ** 3:
#         print(x)

# 方法2
# for x in range(100, 1000):
#     bai = x // 100  # 百位
#     shi = x % 100 // 10  # 十位
#     ge = x % 10  # 个数
#     if x == bai ** 3 + shi ** 3 + ge ** 3:
#         print(x)

# 方法3
for bai in range(1, 10):
    for shi in range(10):
        for ge in range(10):
            # print(bai, shi, ge)
            x = bai * 100 + shi * 10 + ge
            if x == bai ** 3 + shi ** 3 + ge ** 3:
                print(x)

