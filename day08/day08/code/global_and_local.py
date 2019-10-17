# 此示例示意全局变量和局部变量 


a = 10000
def fx():
    b = 20000
    print("fx里面的a=", a)  # 在函数内部可以访问函数外部的
                           # 全局变量
    print("fx里面的b=", b)

print(a)  # 10000
fx()
print(b)  # 不能访问fx函数内部的局部变量b