
# import math
import math as m

r1 = float(input("请输入圆的半径: "))

area1 = m.pi * r1 ** 2
print('半径为', r1, '的圆的面积是:', area1)


area2 = float(input("请输入圆的面积: "))
r2 = m.sqrt(area2 / m.pi)
print("面积为:", area2, '的圆的半径是:', r2)

