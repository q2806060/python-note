# 练习
# class MyRange:
#     def __init__(self, begin, end=None, step=None):
#         if end is None:
#             begin = 0
#             end = begin
#         if step is None:
#             step = 1
#         self.begin = begin
#         self.end = end 
#         self.step = step        
#         self.l = []
#         while self.begin < self.end:
#             self.l.append(self.begin)
#             self.begin += self.step
#     def __iter__(self):
#         return MyRange_next(self.l)

# class MyRange_next:
#     def __init__(self, l):
#         self.l = l
#         self.index = 0

#     def __next__(self):
#         try:
#             x = self.l[self.index]
#         except IndexError:
#             raise StopIteration
#         self.index += 1
#         return x 

# l = list(MyRange(5))
# print(l) #[0, 1, 2, 3, 4]

# print(sum(MyRange(1, 100)))
# for x in MyRange(1, 10, 3):
#     print(x)



# new



class MyRange:
    def __init__(self, begin, end=None, step=None):
        if end is None:
            begin = 0
            end = begin
        if step is None:
            step = 1
        self.begin = begin
        self.end = end 
        self.step = step        

    def __iter__(self):
        return MyRange_next(self.begin, self.end, self.step)

class MyRange_next:
    def __init__(self, begin, end, step):
        self.begin = begin
        self.end = end
        self.step = step

    def __next__(self):
        if self.step > 0:
            if self.begin > self.end:
                raise StopIteration
            r = self.begin
            self.begin += self.step
            return r
        if self.step < 0:
            if self.step < self.end:
                raise StopIteration
            r = self.begin
            self.begin += self.step
            return r


l = list(MyRange(5))
print(l) #[0, 1, 2, 3, 4]

print(sum(MyRange(1, 100)))
for x in MyRange(1, 10, 3):
    print(x)
































































