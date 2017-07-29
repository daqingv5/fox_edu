# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-12 18:23
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170711_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name': '\u8f6e\u64ad\u8bfe\u7a0b',
                'proxy': True,
                'verbose_name_plural': '\u8f6e\u64ad\u8bfe\u7a0b',
            },
            bases=('courses.course',),
        ),
        migrations.RemoveField(
            model_name='course',
            name='learn_times',
        ),
        migrations.RemoveField(
            model_name='course',
            name='teacher_tell',
        ),
        migrations.RemoveField(
            model_name='course',
            name='youneed_know',
        ),
        migrations.AddField(
            model_name='course',
            name='is_banner',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6e\u64ad'),
        ),
        migrations.AddField(
            model_name='course',
            name='learn_time',
            field=models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u65f6\u957f(\u5206\u949f)'),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(default='', max_length=300, verbose_name='\u8bfe\u7a0b\u7c7b\u522b'),
        ),
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u8bfe\u7a0b\u8be6\u60c5'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='courses/%y/%m', verbose_name='\u5c01\u9762\u56fe'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u8bfe\u7a0b\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='course',
            name='tag',
            field=models.CharField(default='', max_length=20, verbose_name='\u8bfe\u7a0b\u6807\u7b7e'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher', verbose_name='\u8bb2\u5e08'),
        ),
    ]