# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-08 07:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='userdcar',
            new_name='usedcar',
        ),
    ]
