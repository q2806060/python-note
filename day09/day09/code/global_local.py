# global_local.py

# 此示例示意全局变量和局部变量的定义方式和访问方式
a = 100
b = 200
def fx(c):
    d = 400
    a = 10000
    print(a, b, c, d)

fx(300)
print('a=', a)
print('b=', b)
# print('c=', c)  # 出错,全局作用域内没有c这个变量

