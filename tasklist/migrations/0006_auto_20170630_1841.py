# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-30 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0005_auto_20170625_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklistimage',
            name='tasklist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasklist.TaskList'),
        ),
    ]
