# if_embed.py

# 输入一个月份,判断这个月是哪儿个季度
s = int(input("请输入月份(1~12): "))

if 1 <= s <= 12:
    print("这是合法的月份")
    if s <= 3:
        print("春季")
    elif s <= 6:
        print("夏季")
    elif s <= 9:
        print("秋季")
    else:
        print("冬季")
else:
    print("您的输入有误")

