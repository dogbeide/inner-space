# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-26 21:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='mesage_html',
            new_name='message_html',
        ),
    ]
