# mylist.py

class MyList(list):
    def __init__(self, *args):
        super(MyList, self).__init__(*args)
        self.append("-----")


myl = MyList(range(3, 6))
myl.append(6)
print(myl)  # [3, 4, 5, 6]