#   1. 写程序算出 1~ 20 的阶乘的和
#     1! + 2! + 3! + 4! + ..... + 20!

def myfac(n):
    if n == 0:
        return 1
    return n * myfac(n - 1)

s = 0
for x in range(1, 21):
    s += myfac(x)
print("和为:", s)

print("和 :", sum(map(myfac, range(1, 21))))

