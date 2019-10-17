# class_variable.py

# 此示例示意类变量的定义和使用方法
class Human:
    total_count = 0  # 类变量,用来记录此类的实例的个数


# 1. 类变量可以通过该类直接访问
print(Human.total_count)  # 0
Human.total_count += 100  # 
print(Human.total_count)  # 100


