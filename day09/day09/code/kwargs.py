# kwargs.py


# 此示例示意双星号字典形参的定义方法和作用
def func(**kwargs):
    print("参数个数是:", len(kwargs))
    print('kwargs =', kwargs)

func(a=1,b=2,c=3)
func()
d1 = {'name':"小张", 'age':20, 'score':100}
func(**d1)  # func(name='小张', age=20, score=100)


