# class_slots.py
# __slots__列表限定Human类型的对象只能有name,age属性
# 不能有其它属性
class Human:
    __slots__ = ['name', 'age']
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_info(self):
        print(self.name, self.age)

s1 = Human('Tarena', 15)
s1.show_info()  # tarena 15
# s1.Age = 16  # 错写了属性名为Age,如果有slots列表,则会报错
s1.show_info()  # tarena 15


