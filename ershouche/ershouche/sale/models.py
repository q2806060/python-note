from django.db import models
from userinfo.models import User


class CarBrand(models.Model):
    brandname = models.CharField("车辆品牌",max_length=30,unique=True)
    brandlogo = models.ImageField(upload_to="static/images")
    isdel = models.BooleanField(default=0)

    def __str__(self):
        return self.brandname

    class Meta:
        db_table = "carbrand"
        verbose_name = "车辆品牌"
        verbose_name_plural = verbose_name

class CarType(models.Model):
    typename = models.CharField("车辆类型",max_length=30,unique=True)
    carbrand = models.ForeignKey(CarBrand)

    def __str__(self):
        return self.typename

    class Meta:
        db_table = "cartype"
        verbose_name = "车辆类型"
        verbose_name_plural = verbose_name

class UsedCar(models.Model):
    carid = models.CharField("车辆编号",max_length=30)
    caryear = models.CharField("买入日期", max_length=20)
    carfixed = models.BooleanField("维修记录",default=0)
    carcolor = models.CharField("颜色",max_length=30,null=True)
    carpushnum = models.DecimalField("排量",max_digits=2,decimal_places=1,default=0)
    carrun = models.FloatField("公里数", default=0)
    carengine = models.CharField("引擎",max_length=50, null=True)
    carprice = models.DecimalField("卖价",max_digits=8,decimal_places=2)
    caraddress = models.CharField("地址",max_length=100)
    carpubdate = models.DateTimeField("发布时间")
    carviews = models.IntegerField("浏览人数")
    carinfo = models.TextField("车况")
    carpic = models.ImageField("图片",upload_to="img/car",default="")
    carhistory = models.TextField("车辆历史")
    carisallowed = models.IntegerField("审核状态",choices=((0,"等待审核"),(1,"正在审核"),(2,"审核通过"),(3,"审核失败")),default=0)
    carofnewprice = models.DecimalField("新车价格",max_digits=8,decimal_places=2)
    carisbuy = models.BooleanField("是否购买", default=False)
    carprocedures = models.BooleanField("手续齐全", default=True)
    cardebt = models.BooleanField("是否有债务", default=False)
    carisdel = models.BooleanField("是否删除订单",default=0)
    cartitle = models.CharField("车名", max_length=50, null=True)
    user = models.ForeignKey(User)
    carbrand = models.ForeignKey(CarBrand,null=True)
    cartype = models.ForeignKey(CarType, null=True)

    def __str__(self):
        return self.carid

    class Meta:
        db_table = "usedcars"
        verbose_name = "二手车"
        verbose_name_plural = verbose_name
