# enclosure.py

# 此示例示意私有属性和私有方法
class A:
    def __init__(self):
        self.__money = 0  # 私有属性,此类以外的方法不能访问

    def show_info(self):
        '方法内可以访问此类对象的私有属性和调用它的私有方法'
        print("钱数:", self.__money)
        self.__m()  # 可以调用私有方法

    def __m(self):
        '私有方法'
        print("A类的__m方法被调用")

a = A()
# print(a.__money)  # 出错,不能访问私有属性
a.show_info()
# a.__m()  # 出错,私有方法不可以在类外调用
