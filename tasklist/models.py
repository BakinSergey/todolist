# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


# список задач
class TaskList(models.Model):

    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(max_length=200, verbose_name='Комментарий')

    status = models.BooleanField(default=False, db_index=True, verbose_name='Статус')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создан')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Последняя Редакция')

    tags = TaggableManager(blank=True, verbose_name='Тэги')

    class Meta:
        unique_together = ('title', 'created')
        ordering = ['created', ]
        verbose_name = 'список задач'
        verbose_name_plural = 'списки задач'

    def __str__(self):
        return '{0}'.format(self.title)

    def get_complete_task_number(self):
        return Task.objects.filter(tasklist=self, status=True).count()

    def get_uncomplete_task_number(self):
        return Task.objects.filter(tasklist=self, status=False).count()

    def get_tasklist_complete_percent(self):
        task_total = Task.objects.filter(tasklist=self).count()
        if task_total != 0:
            task_complete_nmb = Task.objects.filter(tasklist=self, status=True).count()
            percent = (task_complete_nmb/task_total)*100
            if percent == 100:
                self.status = True
            else:
                self.status = False
            self.save()
            return percent
        else:
            return 0


# Картинка к списку задач - не реализовано(формат, проверка на несколько изо к одному списку и т.п)
class TaskListImage(models.Model):
    image = models.ImageField(upload_to='images/')
    tasklist = models.ForeignKey(TaskList, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'картинка'
        verbose_name_plural = 'картинки'


# задача(пункт списка)
class Task(models.Model):
    tasklist = models.ForeignKey(TaskList, on_delete=models.CASCADE, blank=True, null=True, default=None)
    text = models.TextField(max_length=160, verbose_name='Задача')
    status = models.BooleanField(default=False, db_index=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создан')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Редакция')

    def __str__(self):
        return '{0}'.format(self.text)

    class Meta:
        ordering = ['created']
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
