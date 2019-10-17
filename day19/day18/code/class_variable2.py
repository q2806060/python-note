# class_variable2.py

# 此示例示意类变量的定义和使用方法
class Human:
    total_count = 0  # 类变量,用来记录此类的实例的个数


# 2. 类变量可以通过类的实例直接访问(取值)
h1 = Human()  # 创建一个实例
print(h1.total_count)  # 0
h1.total_count = 100  # 创建实例变量的语法
print(h1.total_count)  # 100

print("Human.total_count=", Human.total_count)  # 0



