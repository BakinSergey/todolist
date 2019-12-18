# -*- coding: UTF-8 -*-

from django import forms
from tasklist.models import Task, TaskList, TaskListImage
from taggit.forms import TagField


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['tasklist']

    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=160, label='Текст Задачи')
    status = forms.BooleanField(widget=forms.CheckboxInput, required=False, label='Статус выполнения')


class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = '__all__'
        exclude = ['user', 'status']

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=200,
                            label='Название Списка')
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=200, required=False, label='Комментарий')
    tags = TagField(label='Тэги', required=False)  # , widget=forms.TextInput(attrs={'class': 'form-control'}) стилизовать поле "теги" не получается...


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size': '40', 'class': 'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'size': '40', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    copy = forms.BooleanField(required=False)


class TaskListImageForm(forms.ModelForm):
    class Meta:
        model = TaskListImage
        exclude = ['tasklist']
