
class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __len__(self):
        return len(self.data)
    

L = []
L.append({1, 2, 3})
L.append(("A", "B", "C"))
L.append(MyList([4, 5, 6]))


s = 0
for x in L:
    s += len(x)  # x.__len__()

print("元素个数是:", s)  # 6
print(L)