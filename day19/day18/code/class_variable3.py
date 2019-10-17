# class_variable2.py

# 此示例示意类变量的定义和使用方法
class Human:
    total_count = 0  # 类变量,用来记录此类的实例的个数


# 3. 类变量可以通过此类的对象的__class__属性间接访问
h1 = Human()
print(h1.total_count)  # 0
h1.__class__.total_count += 100  # Human.total_count += 100
print(h1.total_count)  # 100

print(Human.total_count)  # 100


