# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-01 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_auto_20181101_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='birth',
            field=models.DateField(auto_now_add=True),
        ),
    ]