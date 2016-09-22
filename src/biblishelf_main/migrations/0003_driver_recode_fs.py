# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblishelf_main', '0002_auto_extend_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='fs',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='last_online_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='uri',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]