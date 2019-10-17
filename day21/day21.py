#1

# class MyNumber:
#     def __init__(self, value):
#         self.data = value

#     def __repr__(self):
#         return 'MyNumber(%d)' %self.data

#     def __add__(self, other):
#         v = self.data + other.data
#         return MyNumber(v) 

#     def __sub__(self, rhs):
#         v = self.data - rhs.data
#         return MyNumber(v) 


# n1 = MyNumber(200)
# n2 = MyNumber(100)
# n3 = n1 + n2
# n4 = n1 - n2
# print(n1, '+', n2, '=', n3)
# print(n1, '-', n2, '=', n4)


#2

# class MyList:
#     def __init__(self, lst):
#         self.ilist = list(lst)

#     def __repr__(self):
#         return 'MyList(%s)' %self.ilist

#     def __add__(self, rhs):
#         new_list = self.ilist + rhs.ilist
#         return MyList(new_list) 
        
#     def __mul__(self, rhs):
#         new_list = self.ilist * rhs
#         return MyList(new_list)


# l1 = MyList([1, 2, 3])
# l2 = MyList(range(4,6))
# l3 = l1 + l2    
# print(l3)
# l4 = l2 + l1
# print(l4)
# l5 = l1 * 2
# print(l5)


# 练习

class OrderSet:
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def __repr__(self):          #字符串
        return '%s' %self.data

    def __and__(self, rhs):      #集合交集    
        lst = [x for x in self.data if x in rhs.data]
        return OrderSet(lst)
  
    def __or__(self, rhs):       #集合并集
        lst = self.data + [x for x in rhs.data if x not in self.data]
        return OrderSet(lst)

    def __sub__(self, rhs):
        lst = [x for x in self.data if x not in rhs.data]
        return OrderSet(lst)

    def __xor__(self, rhs):      #集合不同部分
        lst = (self - rhs) | (rhs - self)
        return lst

    def __eq__(self, rhs):       #集合是否相等
        return self.data == rhs.data

    def __ne__(self, rhs):       #集合是否不等
        return self.data != rhs.data
    
    def __contians__(self, e):      #集合是否包含元素
        return e in self.data

    def __iter__(self):
        return  OrderSetNext(self.data)

class OrderSetNext:
    def __init__(self, lst):
        self.data = lst
        self.index = 0

    def __next__(self):
        try:
            r = self.data[self.index]
            self.index += 1
        except StopIteration:
            return
        return r
    #测试

s1 = OrderSet([1, 2, 3, 4])
s2 = OrderSet([3, 4, 5])

print(s1 & s2)     #[3, 4]
print(s1 | s2)     #[1, 2, 3, 4, 5]
print(s1 ^ s2)     #[1, 2, 5]
if OrderSet([1, 2, 3]) != OrderSet([1, 2, 3, 4]):
    print('不相等')
if s2 == OrderSet([3, 4, 5]):
    print('s2 == OrderSet([3, 4, 5])')
if 2 in s1:
    print('2 in s1')












































