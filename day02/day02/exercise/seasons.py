#   1. 输入一个季度 1~4,输出这个季度有哪儿几个月份,如果
#     输入的不是1~4的整数,提示用户您输错了

season = int(input("请输入一个季度(1~4): "))

if season == 1:
    print("春度有1,2,3月")
elif season == 2:
    print("夏季有4,5,6月")
elif season == 3:
    print("秋季有7,8,9月")
elif season == 4:
    print("冬季有10, 11, 12月")
else:
    print("您的输入有错!")

