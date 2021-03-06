# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-23 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0002_auto_20170623_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskListImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='tasklist',
            name='image',
        ),
        migrations.AddField(
            model_name='tasklistimage',
            name='tasklist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasklist.TaskList'),
        ),
    ]
