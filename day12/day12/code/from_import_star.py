

# 此示例示意from import *语句的用法
from math import *

r1 = float(input("请输入圆的半径: "))

area1 = pi * r1 ** 2
print('半径为', r1, '的圆的面积是:', area1)


area2 = float(input("请输入圆的面积: "))
r2 = sqrt(area2 / pi)
print("面积为:", area2, '的圆的半径是:', r2)

