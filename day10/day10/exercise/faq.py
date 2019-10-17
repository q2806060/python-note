L = [1, 2, 3]
def f1(lst):
    L = lst  # 可以,创建一个局部变量

def f2(lst):
    L += lst  # 出错,不可以直接操作全局变量

def f3(lst):
    L.extend(lst)  # 可以,操作的是列表对象

f1([4, 5, 6])
# f2([4, 5, 6])
f3([4, 5, 6])
print(L)  # ???
