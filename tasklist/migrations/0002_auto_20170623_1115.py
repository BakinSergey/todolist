# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-23 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Статус'),
        ),
    ]
