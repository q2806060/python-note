from django.db import models
from userinfo.models import Users

ORDERSTATUS = (
    (0,"已出价"),
    (1,"已支付"),
    (2,"交易关闭"),
    (3,"订单关闭"),
    (4,"交易中"),
)
# Create your models here.
class BuyId(models.Model):
    orderno = models.CharField("订单号",max_length=50, null=False)
    buyuser = models.ForeignKey(Users,related_name="buser")
    saleuser = models.ForeignKey(Users,related_name="suser")
    car = models.CharField("车辆信息",max_length=200, null=False)
    price = models.DecimalField("车辆价格",max_digits=8,decimal_places=2)
    date = models.DateTimeField("订单生成时间")
    orderstatus = models.IntegerField("订单状态", choices=ORDERSTATUS, default=0)
    isdelete = models.BooleanField("是否删除", default=False)

    def __str__(self):
        return self.orderno

    class Meta:
        db_table = "buyid"
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name