#   4. BMI指数(Body Mass Index) 又称 身体质量指数
#     BMI值计算公式 : BMI = 体重(公斤) / 身高(米)的平方
#       如:
#         一个69公斤的人,身高是 173公分
#         BMI = 69 / 1.73**2 = 23.05
#     标准表:
#       BMI < 18.5         体重过轻
#       18.5 <= BMI <= 24  正常范围
#       BMI > 24           体重过重
#     要求: 输入身高和体重，打印出BMI的值并打印体重状况

kg = float(input("请输入体重(kg): "))
meter = float(input("请输入身高(米): "))
bmi = kg / meter ** 2
print("BMI=", round(bmi, 2))
if bmi < 18.5:
    print("您的体重过轻!")
elif bmi < 24:
    print("您体重正常!")
else:
    print("您的体重过重!!!")



