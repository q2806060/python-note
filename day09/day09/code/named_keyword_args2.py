# named_keyword_args2.py


def fx(a, b, *args, c=111, d=222):
    print(a, b, args, c, d)

fx(1, 2, 3, 4, d=200, c=100)
fx(1, 2, 3, 4)
fx(1, 2, 3, 4, c=10)
