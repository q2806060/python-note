

s = '''
v = 100

def f1():
    global v  # 声明v是全局作用域的变量, 不是局部变量
    v = 200  # 想让此语句对全局变量进行修改怎么办?

f1()
print(v)  # 100

'''
exec(s)

