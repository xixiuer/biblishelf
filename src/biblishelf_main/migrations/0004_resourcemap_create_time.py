# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblishelf_main', '0003_auto_20160916_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcemap',
            name='create_time',
            field=models.DateTimeField(blank=True, help_text='help check out danger file', null=True),
        ),
    ]
