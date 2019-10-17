# super_init.py

class Human:
    def __init__(self, n, a):
        self.name = n  # 姓名
        self.age = a  # 年龄
        print("Human.__init__被调用")

    def infos(self):
        print("姓名:", self.name)
        print("年龄:", self.age)

class Student(Human):
    def __init__(self, n, a, s=0):
        # self.name, self.age = n, a  # 不符面向对象的编程思想
        super().__init__(n, a)  # 显式调用父类的初始化方法
        self.score = s
        print("Student.__init__被调用!")

    def infos(self):
        super().infos()
        print("成绩:", self.score)

s1 = Student('小李', 18, 98)
s1.infos()

# h1 = Human("小张", 20)
# h1.infos()
