#   2. 求 1 ~ 100之间所有不能被 2或不能被3, 5, 7
#       整除的数的和

s = 0  # 用于累加和
for x in range(1, 101):
    if x % 2 == 0:
        continue
    # 走到此处此数不能被2整除
    if x % 3 == 0:
        continue
    if x % 5 == 0:
        continue
    if x % 7 == 0:
        continue
    # print('----->', x)
    s += x

print("和是:", s)