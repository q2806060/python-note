# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-08 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0005_auto_20190308_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]