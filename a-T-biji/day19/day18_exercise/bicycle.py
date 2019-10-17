#   2. 写一个Bicycle类,用run方法,调用时显示骑行的里程
#     class Bicycle:
#         def run(self, km):
#             print("自行车骑行了", km, '公里')
    
#     再写一个EBicycle(电动自行车), 在Bicycle类的基础上,添加电池
#     电量volume属性,此类有两个方法:
#       fill_charge(vol)  用来充电,vol为电量(度)
#       run(km) 方法 每骑行 10km 消耗1度电,同时显示当前电量,当
#       电量耗尽时则用脚蹬骑行(调用Bicyle的run方法 )
#     class EBicycle(Bicycle):
#          ....
        
#     测试程序:
#     b = EBicycle(5)  # 新买的电动车内有5度电
#     b.run(10)  # 电动骑行了10km 还剩4度电
#     b.run(100) # 电动骑行了40km 还剩0度电  自行车骑行了 60 公里
#     b.fill_charge(10)  # 电动自行车充电10度
#     b.run(50)  # 电动骑行了50km 还剩5度电



class Bicycle:
    def run(self, km):
        print("自行车骑行了", km, '公里')

class EBicycle(Bicycle):
    def __init__(self, v):
        self.volume = v  # 初始电量

    def run(self, km):
        e_km = min(km , self.volume * 10)  # 取电行驶公里数
        self.volume -= e_km / 10
        if e_km > 0:
            print("电动骑行了%dkm, 还剩%d度电" %
                     (e_km, self.volume))
        if km > e_km:  # 没电时调用父类的方法
            super().run(km - e_km)
    
    def fill_charge(self, vol):
        self.volume += vol  # 充电
        print("电动自行车充电%d度" % vol)

b = EBicycle(5)  # 新买的电动车内有5度电
b.run(10)  # 电动骑行了10km 还剩4度电
b.run(100) # 电动骑行了40km 还剩0度电  自行车骑行了 60 公里
b.fill_charge(10)  # 电动自行车充电10度
b.run(50)  # 电动骑行了50km 还剩5度电
