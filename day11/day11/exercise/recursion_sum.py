# 练习:
#   写一个递归求和的函数 recursion_sum(n)
#   此函数返回 1 + 2 + 3 + 4 + .... + n的和

#   def recursion_sum(n):
#       ...  # 此外自己实现
#   print(recursion_sum(100))  # 5050

# recursion_sum(5) = 5 + (4 + 3 + 2 + 1)
#                  = 5 + recursion_sum(4)
# recursion_sum(4) = 4 + (3 + 2 + 1)
#                  = 4 + recursion_sum(3)

def recursion_sum(n):
    # 当n == 1 和为1
    # 否则 n的和等同于 n + (n-1)的和
    if n == 1:
        return 1
    else:
        return n + recursion_sum(n - 1)

print(recursion_sum(5))
# print(recursion_sum(100))  # 5050
