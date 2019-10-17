class Bicycle:
    def run(self, km):
        print('自行车骑了', km, '公里.')
class EBicycle(Bicycle):
    def __init__(self, vol):
        self.vol = vol
        print('车内还有', self.vol, '度电.')
    def fill_charge(self, vol):                           
        self.vol += vol        
        print('充电', vol, '度.')
    def run(self, km):
        if self.vol >= km / 10:
            self.vol -= km / 10
            print('骑行了', km, '公里，还剩', self.vol, '度电.')
        else:
            km0 = self.vol * 10
            km -= self.vol *10
            self.vol = 0
            print('骑行了', km0, '公里，还剩', self.vol, '度电.', end ='')
            super().run(km)
b = EBicycle(5)         #新买的电动车内有5度电
b.run(10)               #电动车骑了10km，还剩4度电
b.run(100)              #骑了40km ,还剩0度电，自行车骑了60公里
b.fill_charge(10)       #充电10度
b.run(50)               #骑行50公里，还剩5度电

















































