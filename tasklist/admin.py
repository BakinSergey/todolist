# -*- coding: utf-8 -*-

from django.contrib import admin
from tasklist.models import *


class TaskInListInline(admin.TabularInline):
    model = Task
    extra = 0


class TaskListImageInline(admin.TabularInline):
    model = TaskListImage
    extra = 0


class TaskAdmin(admin.ModelAdmin):
    list_display = ('text', 'created', 'updated', 'status')
    search_fields = ['text']

    class Meta:
        model = Task

admin.site.register(Task, TaskAdmin)


class TaskListAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TaskList._meta.fields]
    search_fields = ['title', 'created']
    inlines = [TaskInListInline, TaskListImageInline]

    class Meta:
        model = TaskList

admin.site.register(TaskList, TaskListAdmin)


class TaskListImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TaskListImage._meta.fields]

admin.site.register(TaskListImage, TaskListImageAdmin)
