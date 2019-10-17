from django.db import models

# Create your models here.

#创建一个实体类 - Publisher,表示出版社信息
#注意：主键&自增，在Django ORM中会自动创建
#1.name:出版社的名称 - varchar
#2.address:出版社的地址 - varchar
#3.city:出版社的所在城市 - varchar
#4.country:出版社所在的国家 - varchar
#5.website:出版社网址 - varchar

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    website = models.URLField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "publisher"
        verbose_name = "出版社"
        verbose_name_plural = verbose_name
    
class Author(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True, db_index=True, verbose_name="姓名")
    age = models.IntegerField(null=False, verbose_name="年龄")
    email = models.EmailField(null=True, verbose_name="邮箱")
    isActive = models.BooleanField(default=True, verbose_name="激活")

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "author"
        verbose_name = "作者"
        verbose_name_plural = verbose_name

class Book(models.Model):
    title = models.CharField(max_length=30, null=False, unique=True, db_index=True)
    publicate_date = models.DateTimeField(null=False, db_index=True)
    publisher = models.ForeignKey(Publisher, null=True)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"
        verbose_name = "书籍"
        verbose_name_plural = verbose_name

class Wife(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    author = models.OneToOneField(Author)