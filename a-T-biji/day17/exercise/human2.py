# 练习:
#   有两个人:
#     1. 姓名: 张三, 年龄: 35
#     2. 姓名: 李四, 年龄: 10
#   行为:
#     1. 教别人学东西 teach
#     2. 工作赚钱  work
#     3. 借钱 borrow
#     4. 显示自己的信息 show_info
#   事情:
#     张三 教 李四 学 python
#     李四 教 张三 学 王者荣耀
#     张三 上班赚钱 1000 元
#     李四 向 张三 借钱 200元
#     35 岁的 张三 有钱 800 元,它学会的技能是: 王者荣耀
#     10 岁的 李四 有钱 200 元,它学会的技能是: python
#   类的封装如下:
#     class Human:
#         def __init__(self, ....):
#             ...
#         ...
#     zhang3 = Human("张三", 35)
#     li4 = Human("李四", 10)
#     .... 此处描述事情的过程




class Human:
    def __init__(self, name, age):
        self.name = name  # 姓名
        self.age = age  # 年龄
        self.money = 0  # 钱
        self.skill = []  # 此列表用来存储技能

    def teach(self, other, skill):
        print(self.name, '教', other.name, '学',
              skill)
        other.skill.append(skill)  # 添加技能

    def work(self, m):
        print(self.name, '上班赚钱', m, '元')
        self.money += m  # 钱增多了

    def borrow(self, other, money):
        # 如果other 的 money 大于money, 借钱成功
        if other.money > money:
            print(self.name, '向', other.name,
            '借钱', money, '元')
            other.money -= money  # 实现借钱的逻辑
            self.money += money
        else:
            print(self.name, '向', other.name,
                  '借钱失败')
        
    def show_info(self):
        print(self.age, '岁的', self.name,
              '有钱', self.money, '元,它学会的技能是:',
              self.skill)

zhang3 = Human("张三", 35)
li4 = Human("李四", 10)
# 张三 教 李四 学 python
zhang3.teach(li4, 'python')
# 李四 教 张三 学 王者荣耀
li4.teach(zhang3, "王者荣耀")
# 张三 上班赚钱 1000 元
zhang3.work(1000)
# 李四 向 张三 借钱 200元
li4.borrow(zhang3, 200)
# 35 岁的 张三 有钱 800 元,它学会的技能是: 王者荣耀
zhang3.show_info()
# 10 岁的 李四 有钱 200 元,它学会的技能是: python
li4.show_info()

