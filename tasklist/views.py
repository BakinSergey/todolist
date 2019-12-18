# -*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.urls import reverse


from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from tasklist.forms import TaskForm, TaskListForm
from tasklist.models import TaskList, Task

from generic.mixins import PageNumberMixin
from django.db.models import Q

from functools import reduce
import operator

# Create your views here.


# ===================================================  TaskList  ================================================

class TaskListIndex(ListView):

    model = TaskList
    template_name = 'tasklist_index.html'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super(TaskListIndex, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        qs = super(TaskListIndex, self).get_queryset().filter(user=self.request.user).order_by('-created')

        search_query = self.request.GET.get('q')
        if search_query:
            query_list = search_query.split()
            qs = qs.filter(
                reduce(operator.__and__, (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.__and__, (Q(description__icontains=q) for q in query_list))
            )
        return qs


# TaskList Create, Detail, Delete
class TaskListCreate(CreateView):

    model = TaskList
    template_name = 'tasklist_create.html'
    form_class = TaskListForm

    def get_context_data(self, **kwargs):
        context = super(TaskListCreate, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return super(TaskListCreate, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(TaskListCreate, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('tasklist_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.user = self.request.user
        form.save(commit=True)
        return super(TaskListCreate, self).form_valid(form)


class TaskListDetail(TemplateView, PageNumberMixin):

    template_name = 'tasklist_detail.html'
    pk_url_kwarg = 'pk'
    form = None
    tasklist = None

    def get_context_data(self, *args, **kwargs):
        context = super(TaskListDetail, self).get_context_data(**kwargs)
        tasks = self.tasklist.task_set.all()
        context['form'] = self.form
        context['tasks'] = tasks
        context['tasklist'] = self.tasklist

        return context

    def get(self, request, *args, **kwargs):
        self.tasklist = TaskList.objects.get(pk=self.kwargs['pk'])
        self.form = TaskListForm(instance=self.tasklist)

        return super(TaskListDetail, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if self.form.is_valid():
            self.form.save()
            return redirect(reverse('tasklist_index'))
        else:
            return super(TaskListDetail, self).get(request, *args, **kwargs)


class TaskListDelete(DeleteView):

    model = TaskList
    template_name = 'tasklist_delete.html'

    def post(self, request, *args, **kwargs):
        self.success_url = reverse('tasklist_index')

        return super(TaskListDelete, self).post(request, *args, **kwargs)


# ===================================================  Task  ================================================
class TaskCreate(CreateView):

    model = Task
    template_name = 'task_add.html'
    form_class = TaskForm

    def get(self, request, *args, **kwargs):
        if self.kwargs['pk']:
            self.initial['tasklist'] = TaskList.objects.get(pk=self.kwargs['pk'])
        return super(TaskCreate, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TaskCreate, self).get_context_data(**kwargs)
        tasklist = TaskList.objects.get(pk=self.kwargs['pk'])
        context['tasklist'] = tasklist  # для крошек
        return context

    def post(self, request, *args, **kwargs):
            return super(TaskCreate, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('tasklist_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.tasklist = TaskList.objects.get(pk=self.kwargs['pk'])
        form.save()
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(UpdateView):

    model = Task
    template_name = 'task_edit.html'
    form_class = TaskForm
    pk_url_kwarg = 'upd'

    def get_context_data(self, **kwargs):
        context = super(TaskUpdate, self).get_context_data(**kwargs)
        task = Task.objects.get(pk=self.kwargs['upd'])
        context['tasklist'] = task.tasklist

        return context

    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=self.kwargs['upd'])
        self.form = TaskForm(request.POST, instance=task)

        if self.form.is_valid():
            self.form.save()
        self.success_url = reverse('tasklist_detail', kwargs={'pk': Task.objects.get(pk=kwargs['upd']).tasklist.id})

        return super(TaskUpdate, self).post(request, *args, **kwargs)


class TaskDelete(DeleteView):

    model = Task
    template_name = 'task_delete.html'
    pk_url_kwarg = 'del'

    def post(self, request, *args, **kwargs):
        self.success_url = reverse('tasklist_detail', kwargs={'pk': self.kwargs['pk']})

        return super(TaskDelete, self).post(request, *args, **kwargs)

