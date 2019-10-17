# 思考:
#   list 类里只有apend向末尾加一个元素的方法,但没有向列表头部
#   添加元素的方法,试想能否为列表在不改变原有功能的基础上添加一
#   个 insert_head(n) 方法在列表的头部添加新元素

#     class MyList(list):
#         def insert_head(self, n):
#              ....  # 此自己偿试写代码

#     myl = MyList(range(3, 6))
#     print(myl)  # [3, 4, 5]
#     myl.insert_head(2)
#     print(myl)  # [2, 3, 4, 5]
#     myl.append(6)
#     print(myl)  # [2, 3, 4, 5, 6]




class MyList(list):
    def insert_head(self, n):
        # self[0:0] = [n]  # 用切片头插
        self.insert(0, n)  # 用list的方法来头插
        # self.insert_head(n)  # 递归... 会出错

myl = MyList(range(3, 6))
print(myl)  # [3, 4, 5]

myl.insert_head(2)
print(myl)  # [2, 3, 4, 5]

myl.append(6)
print(myl)  # [2, 3, 4, 5, 6]
