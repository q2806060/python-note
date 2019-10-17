# init_method.py


# 此示例示意用初始化方法来为Car类创建实例变量(属性)
class Car:
    '''此类用于描述小汽车的行为'''
    def __init__(self, c, b, m):
        self.color = c  # 创建颜色属性
        self.brand = b  # 品牌
        self.model = m  # 型号
        print("初始化方法被调用!!!!")

    def run(self, speed):
        print(self.color, '的', self.brand, 
              self.model, 
              '正在以', speed, '公里/小时的速度行驶')

a4 = Car('红色', '奥迪', 'A4')
a4.run(199)



