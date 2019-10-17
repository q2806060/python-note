# 练习:
#   输入一段字符串,打印出这个字符串中出现过的字符及出现的次数
#   如:
#     输入: ABCDABCABA
#     输出:
#       A: 4次
#       B: 3次
#       D: 1次
#       C: 2次
#       注: 不要求打印的顺序

s = input("请输入文字: ")

d = {}
for ch in s:
    # 如果ch第一次出现,不在d中
    # 把ch加入到d中,值为1
    if ch not in d:
        d[ch] = 1
    else:  # 已经出现过
        d[ch] += 1

# print(d)
for ch, count in d.items():
    print(ch, ":", count, "次")
    

