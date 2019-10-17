# named_keyword_args.py

def func1(a, b, *, c, d):
    '''强制让c,d传参时必须用关键字传参
    让c,d成为命名关键字形参'''
    print(a, b, c, d)

func1(1, 2, c=3, d=4)
func1(a=11, b=22, c=33, d=44)
func1(111, 222, **{"c":333}, d=444)

