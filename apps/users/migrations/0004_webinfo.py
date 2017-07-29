# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-14 11:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170706_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('top_logo', models.ImageField(upload_to='logo/%Y/%m', verbose_name='\u9876\u90e8logo')),
                ('foot_logo', models.ImageField(upload_to='logo/%Y/%m', verbose_name='\u5e95\u90e8logo')),
                ('foot_code', models.ImageField(upload_to='logo/%Y/%m', verbose_name='\u5e95\u90e8\u4e8c\u7ef4\u7801')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7f51\u7ad9\u4fe1\u606f',
                'verbose_name_plural': '\u7f51\u7ad9\u4fe1\u606f',
            },
        ),
    ]