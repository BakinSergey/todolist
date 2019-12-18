# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from tasklist.forms import ContactForm


class Entrance(TemplateView):
    template_name = 'registration/EntrancePage.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Entrance, self).get_context_data(**kwargs)
        return context


class RegisterView(FormView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)


def contactview(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipients = ['serstd@yandex.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, 'sab43@list.ru', recipients)
            except BadHeaderError: #ошибки
                return HttpResponse('Invalid header found')
            return render(request, 'generic/contact_thanx.html')
    else:
        form = ContactForm()
    return render(request, 'generic/contact.html', {'form': form})
