#   # ------- 以下用列表实现-----------
#   L = [1, 2, 3]
#   def f1(lst):
#       lst += [4, 5, 6]
#   f1(L)
#   print(L)  # [1, 2, 3, 4, 5, 6????]

#   # ------- 以下用元组实现-----------
#   L = (1, 2, 3)
#   def f1(lst):
#       lst += (4, 5, 6)
#   f1(L)
#   print(L)  # [1, 2, 3, 4, 5, 6????]

# ------- 以下用列表实现-----------
L = [1, 2, 3]
def f1(lst):
    lst += [4, 5, 6]
f1(L)
print(L)  # [1, 2, 3, 4, 5, 6????]

# ------- 以下用元组实现-----------
L = (1, 2, 3)
def f1(lst):
    lst += (4, 5, 6)
f1(L)
print(L)  # [1, 2, 3, 4, 5, 6????]



class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)
    
    def __repr__(self):
        return "MyList(%s)" % self.data

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)
    
    # def __iadd__(self, rhs):
    #     self.data.extend(rhs.data)
    #     return self


L = MyList([1, 2, 3])
def f1(lst):
    lst += MyList([4, 5, 6])
f1(L)
print(L)  # ???

