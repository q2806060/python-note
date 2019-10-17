# instance_method.py

# 此示例示意实例方法的定义和调用
class Dog:
    '''这是一种小动物的定义'''
    def eat(self, food):
        '''此方法用来描述小狗吃的行为'''
        print('id为', id(self), "的小狗正在吃", food)

    def sleep(self, hour):
        print('id为', id(self), '的小狗睡了',
              hour, '小时')
    
dog1 = Dog()  # 创建一个对象
dog1.eat('骨头')

dog2 = Dog()  # 创建另一个对象
dog2.eat('狗粮')

dog1.sleep(1)
dog2.sleep(3)
Dog.eat(dog1, '包子')  #等同于 dog1.eat("包子")


