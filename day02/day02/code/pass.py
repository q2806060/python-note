# pass.py


# 输入一个学生的成绩 0 ~ 100 之间范围,如果不在此区间,
# 打印错误信息
score = float(input("请输入成绩: "))

if 0 <= score <= 100:
    # print("成绩合法")
    pass  # 又名空语句
else:
    print("成绩不合法,有错!!!")
