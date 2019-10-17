from django.db import models

# Create your models here.
class Users(models.Model):
    uphone = models.CharField(max_length=11)
    upwd = models.CharField(max_length=50)
    uemail = models.CharField(max_length=245)
    uname = models.CharField(max_length=20)
    isActive = models.BooleanField(default=True)
    