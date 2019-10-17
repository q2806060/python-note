# 练习:
#   1. 任意输入一段字符串
#     1) 计算出这个字符串中空格的个数,打印这个数
#        (要求: 用 for语句,不允许使用S.count方法)
#     2) 计算出字符串中,全部英文字符的个数
#        注: 英文字符的编码值为: 0 ~ 127
    
#     思考:
#       用while语句能否实现上述功能?

s = input("请输入一段字符串: ")

blank_count = 0  # 此变量用来记录空格的个数
for ch in s:
    if ch == ' ':
        blank_count += 1
print("空格的个数是: ", blank_count)

english_count = 0  # 此变量用来记录英文字符的个数
for ch in s:
    if 0 <= ord(ch) <= 127:  # if ord(ch) <= 127:
        english_count += 1

print("英文字符的个数是:", english_count)