# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-11 00:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20170711_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='org',
        ),
    ]
