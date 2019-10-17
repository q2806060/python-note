# eval2.py

x = 100
y = 200
s = "x + y"

v2 = eval(s)  # 此处使用当前的作用域的变量作为运行环境
print('v2=', v2)  # 300

global_dict = {'x': 10, 'y': 20}
v3 = eval(s, global_dict)
print('v3=', v3)  # 30

local_dict = {'x':1, 'y':2}
v4 = eval(s, global_dict, local_dict)
print('v4=', v4)  # 3

v5 = eval(s, None, local_dict)
print('v5=', v5)

v6 = eval(s, global_dict, {'x':1})
print('v6=', v6)  # 21

