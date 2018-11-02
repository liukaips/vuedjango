# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-11 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auths', models.CharField(blank=True, max_length=1000, null=True)),
                ('authCase', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AuthScript1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_name', models.CharField(blank=True, max_length=100, null=True)),
                ('auth_file', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]