# -*- coding: utf-8 -*-

from django.conf.urls import url
from tasklist.views import TaskListIndex, TaskListCreate, TaskListDetail, TaskListDelete
from tasklist.views import TaskCreate, TaskUpdate, TaskDelete
from django.contrib.auth.views import login_required

# from django.views.decorators.cache import cache_control

# cache_control(private=True, must_revalidate=True, max_age=3600)

urlpatterns = [
    # TaskList
    url(r'^index/$',              login_required(TaskListIndex.as_view()),        name='tasklist_index'),
    url(r'^create/$',             login_required(TaskListCreate.as_view()),       name='tasklist_create'),
    url(r'^(?P<pk>\d+)/detail/$', login_required(TaskListDetail.as_view()),       name='tasklist_detail'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(TaskListDelete.as_view()),       name='tasklist_delete'),

    # Task
    url(r'^(?P<pk>\d+)/task_add$',                  login_required(TaskCreate.as_view()),  name='task_add'),
    url(r'^(?P<pk>\d+)/task/(?P<upd>\d+)/edit$',    login_required(TaskUpdate.as_view()),  name='task_edit'),
    url(r'^(?P<pk>\d+)/task/(?P<del>\d+)/delete$',  login_required(TaskDelete.as_view()),  name='task_delete'),


    ]
