# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-30 00:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('description_html', models.TextField(blank=True, default='', editable=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CommunityMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Members', to='communities.Community')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_communities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='community',
            name='members',
            field=models.ManyToManyField(through='communities.CommunityMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='communitymember',
            unique_together=set([('community', 'user')]),
        ),
    ]
