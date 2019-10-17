# poly.py

class Shape:  # 图形
    def draw(self):
        print("Shape.draw被调用")

class Point(Shape):  # 点
    def draw(self):
        print("Point.draw被调用")

class Circle(Point):  # 圆
    def draw(self):
        print("Circle.draw被调用")


def my_draw(s):
    s.draw()  # 请问调用哪儿个方法?

s1 = Circle()
s2 = Point()
my_draw(s2)
my_draw(s1)