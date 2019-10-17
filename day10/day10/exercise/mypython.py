#   自己写一个程序的解释执行器,解释执行我们自己输入的程序
#     如:
#       请输入程序: >>> x = 100<回车>
#       请输入程序: >>> y = 200<回车>
#       请输入程序: >>> print("x+y=",x+y)<回车>
#       x+y= 300
#     提示用: exec函数

local_dict = {}

while True:
    s = input("请输入程序: >>> ")
    if s == 'quit()':
        break
    exec(s, None, local_dict)

print(local_dict)
