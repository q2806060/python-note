# 练习:
#   写一个函数,mymax, 此函数可以传入任意个实参,返回实参中的
#   最大数
#   def mymax(...):
#       ....

#   print(mymax(4, 6, 9, 3))  # 9
#   print(mymax("ABC", "abc", '123'))  # abc
#   print(mymax(1,2,3,4,5,6,7,8,9))  # 9

def mymax(*args):
    # return max(args)  # 等同于return max( (4,6,9,3) )
    return max(*args)  # 等同于return max(4, 6, 9, 3)

print(mymax(4, 6, 9, 3))  # 9
print(mymax("ABC", "abc", '123'))  # abc
print(mymax(1,2,3,4,5,6,7,8,9))  # 9

  