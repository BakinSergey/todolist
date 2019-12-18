# -*- coding: utf-8 -*-

from tasklist.models import TaskList, User


def total_tasklist_context(request):
    context = dict()
    context['user_total_nmb'] = User.objects.count()

    site_tasklists = TaskList.objects.all()

    total_tasklist_number = site_tasklists.count()
    complete_tasklist_number = site_tasklists.filter(status=True).count()
    earliest_created_tasklist = site_tasklists.earliest('created')
    latest_created_tasklist = site_tasklists.latest('created')

    context['ttn'] = total_tasklist_number
    context['ctn'] = complete_tasklist_number
    context['ect'] = earliest_created_tasklist
    context['lct'] = latest_created_tasklist

    return context


def user_tasklist_context(request):
    context = dict()
    user = request.user

    if user.is_authenticated:
        user_tasklists = TaskList.objects.filter(user=user)
        if user_tasklists.count() != 0:
            u_total_tasklist_number = user_tasklists.count()
            u_complete_tasklist_number = user_tasklists.filter(status=True).count()
            u_earliest_created_tasklist = user_tasklists.earliest('created')
            u_latest_created_tasklist = user_tasklists.latest('created')

            context['u_ttn'] = u_total_tasklist_number
            context['u_ctn'] = u_complete_tasklist_number
            context['u_ect'] = u_earliest_created_tasklist
            context['u_lct'] = u_latest_created_tasklist

    return context
