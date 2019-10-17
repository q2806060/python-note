# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-08 08:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandname', models.CharField(max_length=30, unique=True, verbose_name='车辆品牌')),
                ('brandlogo', models.ImageField(upload_to='static/images')),
                ('isdel', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': '车辆品牌',
                'verbose_name_plural': '车辆品牌',
                'db_table': 'carbrand',
            },
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=30, unique=True, verbose_name='车辆类型')),
                ('carbrand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.CarBrand')),
            ],
            options={
                'verbose_name': '车辆类型',
                'verbose_name_plural': '车辆类型',
                'db_table': 'cartype',
            },
        ),
        migrations.CreateModel(
            name='UsedCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carid', models.CharField(max_length=30)),
                ('caryear', models.DateTimeField()),
                ('carfixed', models.BooleanField(default=0)),
                ('carcolor', models.CharField(max_length=30, null=True)),
                ('carpushnum', models.FloatField(null=True)),
                ('carrun', models.FloatField(null=True)),
                ('carengine', models.CharField(max_length=50, null=True)),
                ('carprice', models.FloatField()),
                ('caraddress', models.CharField(max_length=100)),
                ('carpubdate', models.DateTimeField()),
                ('carviews', models.IntegerField()),
                ('carinfo', models.TextField()),
                ('carhistory', models.TextField()),
                ('carisallowed', models.CharField(choices=[(0, '等待审核'), (1, '正在审核'), (2, '审核通过'), (3, '审核失败')], default=0, max_length=6, verbose_name='审核状态')),
                ('carofnewprice', models.FloatField()),
                ('carisdel', models.BooleanField(default=0)),
                ('userinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '二手车',
                'verbose_name_plural': '二手车',
                'db_table': 'usedcar',
            },
        ),
        migrations.AddField(
            model_name='cartype',
            name='usedcar',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sale.UsedCar'),
        ),
        migrations.AddField(
            model_name='carbrand',
            name='usedcar',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sale.UsedCar'),
        ),
    ]