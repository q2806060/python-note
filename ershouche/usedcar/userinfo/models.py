from django.db import models
from django.contrib.auth.models import AbstractUser
from sale.models import UsedCars

# Create your models here.

class Users(AbstractUser):
    loginname = models.CharField(max_length=30)
    uemail = models.EmailField(null=True)
    callphone = models.CharField(max_length=11, null=True, blank=True, unique=True)
    idcard = models.CharField('身份证', max_length=20, blank=True, null=True)
    sex = models.IntegerField('性别', choices=((1,'男'),(0,'女')), default=1)
    address = models.CharField("地址", max_length=150,null=True,blank=True)
    logindate = models.IntegerField(default=0)
    birthday = models.DateField(null=True)
    wechat = models.CharField(max_length=30, null=True)
    qq = models.CharField(max_length=15,null=True)
    balance = models.FloatField(default=0)
    allowbuy = models.BooleanField(default=1)
    agreeservice = models.BooleanField(default=0)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "Users"
        verbose_name = "用户信息表"
        verbose_name_plural = verbose_name

CARDTYPE = (
    (0,"储蓄卡"),
    (1,"信用卡"),
)
CARDBANK = (
    (0, "中国银行"),
    (1, "工商银行"),
)
CARDSTATUS = (
    (0,"余额不足"),
    (1,"可以支付"),
)
class UserCard(models.Model):
    cardid = models.CharField("卡号", max_length=30,null=False)
    cardname = models.CharField("开户名",max_length=30, null=False)
    cardtype = models.IntegerField("银行卡类型", choices=CARDTYPE, default=0) 
    cardbank = models.IntegerField("开户行", choices=CARDBANK, default=0)
    cardstatus = models.IntegerField("银行卡状态", choices=CARDSTATUS, default=0)
    user =  models.ForeignKey(Users)

    def __str__(self):
        return self.cardname

    class Meta:
        db_table = "usercard"
        verbose_name = "用户银行卡表"
        verbose_name_plural = verbose_name

class SysMsg(models.Model):
    sysmsgno = models.CharField("系统信息编号",max_length=30,unique=True)
    pubdate = models.DateTimeField("发送时间")
    msginfo = models.TextField("发送内容")
    user = models.ForeignKey(Users)

    def __str__(self):
        return self.sysmsgno

    class Meta:
        db_table = "sysmsg"
        verbose_name = "系统留言"
        verbose_name_plural = verbose_name

class LeaveMsg(models.Model):
    leavemsgno = models.CharField("用户留言编号", max_length=30,unique=True)
    pubdate = models.DateTimeField("发送时间")
    msg = models.TextField("用户留言")
    user = models.ManyToManyField(Users)
    carid = models.ForeignKey(UsedCars)

    def __str__(self):
        return self.leavemsgno

    class Meta:
        db_table = "leavemsg"
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name

class replyMsg(models.Model):
    replymsgno = models.CharField("用户回复编号",max_length=30,unique=True)
    pubdate = models.DateTimeField("发送时间")
    msg = models.TextField("用户回复")
    user = models.ForeignKey(Users)
    lmsgid = models.ForeignKey(LeaveMsg)

    def __str__(self):
        return self.replymsgno

    class Meta:
        db_table = "replymsg"
        verbose_name = "回复信息"
        verbose_name_plural = verbose_name

