# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-04 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20171103_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.PositiveIntegerField(default=1526538688),
        ),
    ]
