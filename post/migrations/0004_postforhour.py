# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-18 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20170717_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostForHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2020)),
                ('title', models.TextField(max_length=30)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
