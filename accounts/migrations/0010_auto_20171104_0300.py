# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-04 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20171104_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.PositiveIntegerField(default=1682610571),
        ),
    ]