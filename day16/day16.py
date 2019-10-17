#1

# def even(start, stop):
#     while start < stop:
#         if start % 2 == 0:
#             yield start
#         start += 1


# for x in even(1, 10):
#     print(x)

# l = [x ** 2 for x in even(10,20)]
# print(l)

# it = iter(even(3, 10))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


#2

# l = [2, 3, 5, 7]
# def f1(l):
#     for i in l:
#         yield i ** 2 + 1
# for i in f1(l):
#     print(i)

# it1 = (x ** 2 + 1 for x in l)
# for i in it1:
#     print(i)

# l = [x ** 2 + 1 for x in l]
# print(l)



#3

# def myfilter(fn, iterable):
#     for i in iterable:
#         if fn(i):            
#             yield i


# def myfilter(fn, iterable):
#     it = iter(iterable)
#     while True:
#         try:
#             i = next(it)
#             if fn(i):            
#                 yield i
#         except StopIteration:
#             break

# for x in myfilter(lambda y : y % 2 == 1, range(10)):
#     print(x)
    

#4

# l = [2, 3, 5, 7]
# A = [x * 10 for x in l]
# it = iter(A)
# print(next(it))
# l[1] = 333
# print(next(it))

# l = [2, 3, 5, 7]
# A = (x * 10 for x in l)
# it = iter(A)
# print(next(it))
# l[1] = 333
# print(next(it))
 

#5

# def myenumerate(iterable, start = 0):
#     for i in iterable:
#         site = start
#         yield (site, i)
#         start += 1

# d = dict(myenumerate('ABCDE', 1))
# print(d)


# def myzip(iter1, iter2):
#     it1 = iter(iter1)
#     it2 = iter(iter2)
#     while True:
#         try:
#             v1 = next(it1)
#             v2 = next(it2)
#         except StopIteration:
#             return
#         yield (v1, v2)

# d = dict(myzip('ABC', '123'))
# print(d)



#6

# s = input('请输入：')
# b = s.encode(encoding = 'utf-8')
# print(len(s))
# print(len(b))
# s2 = b.decode(encoding = 'utf-8')


# 练习

# def myxrange(start, stop = None, step = None):    
#     if stop is None:
#         stop = start
#         start = 0
#     if step == None:
#         step = 1
#     if step > 0:
#         i = start
#         while i < stop:
#             yield i
#             i += step
#     elif step < 0:
#         i = start
#         while i > stop:
#             yield i
#             i += step

# s = (x ** 2 for x in myxrange(1,10,2))
# print(sum(s))



# def isprime(x):
#     if x < 2:
#         return False
#     else:
#         for i in range(2, x):
#             if x % i == 0:
#                 return False
#             else:
#                 return True

# def print_isprimes(n, i = 1):
#     while n > 0:       
#         if isprime(i) == True:
#             yield i
#             n -= 1
#             i += 1
#         else:
#             i += 1
# for i in print_isprimes(5):         
#     print(i)












































































