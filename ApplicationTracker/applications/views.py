from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.db.models.functions import Cast
from django.db.models.fields import DateField
from django.db.models import Count
from events.models import Event
from .models import Application
from collections import namedtuple
import datetime

def get_form_data(post_request):
    application_fields = ['position', 'company', 'location', 'department', 'company_url', 'posting_url', 'portal_url', 'portal_login', 'portal_pass', 'posted_on', 'closes_on', 'applied_on', 'resume', 'cover_letter', 'body']
    form_data = {'user': post_request.user, 'last_updated': datetime.datetime.now()}
    for field in application_fields:
        try:
            if post_request.POST[field] != "":
                form_data[field] = post_request.POST[field]
        except:
            pass
    return form_data

def get_progress(event_type):
    if event_type == 'Job Offer':
        return 100
    elif event_type == 'On Site Interview':
        return 88
    elif event_type == 'Technical Interview':
        return 75
    elif event_type == 'Phone Screen':
        return 45
    elif event_type == 'Application Submitted':
        return 25
    else:
        return 0

def get_icon(event_type):
    if event_type == 'Job Offer':
        return 'icon-dollar'
    elif event_type == 'On Site Interview':
        return 'icon-map-marker'
    elif event_type == 'Technical Interview':
        return 'icon-wrench'
    elif event_type == 'Phone Screen':
        return 'icon-phone'
    elif event_type == 'Application Submitted':
        return 'icon-ok-circle'
    else:
        return 'icon-question-sign'



@login_required
def index(request, status='all'):
    all_applications = Application.objects.filter(user=request.user).order_by('-last_updated').annotate(number_of_events=Count('event'), date=Cast('last_updated', DateField()))

    if status == 'all':
        applications = all_applications
    else:
        applications = Application.objects.filter(user=request.user, status=status).annotate(number_of_events=Count('event'), date=Cast('last_updated', DateField()))

    status_count = {
        'Job_Offer': 0,
        'On_Site_Interview': 0,
        'Technical_Interview': 0,
        'Phone_Screen': 0,
        'Application_Submitted': 0,
        'All': len(all_applications)
    }

    for app in applications:
        if app.status:
            app.progress = get_progress(app.status)
            app.icon = get_icon(app.status)
        else:
            app.progress = 0
            app.icon = 'icon-question-sign'
        if Event.objects.filter(application = app):
            app.recent_event = Event.objects.filter(application = app).latest('event_date')
        else:
            app.recent_event = 'This application has no events'

    for application in all_applications:
        if application.status:
            status = application.status.replace(' ', '_')
            status_count[status] += 1
            
    data = namedtuple('Data', status_count.keys())(**status_count)

    context = {
        'applications': applications,
        'recent_apps': all_applications[:3],
        'template_data': data
    }

    return render(request, 'applications/application-list.html', context)

@login_required
def detail(request, application_id):
    application = get_object_or_404(Application, pk=application_id, user=request.user)
    events = Event.objects.order_by('-event_date', '-id').filter(application=application)
    progress = get_progress(application.status)

    context = {
        'application': application,
        'events': events,
        'progress': progress
    }

    return render(request, 'applications/application-detail.html', context)

@login_required
def add(request):
    if request.method == 'POST':
        application_data = get_form_data(request)
        new_application = Application.objects.create(**application_data)
        default_event = Event.objects.create(application=new_application, event_type='Application Submitted', event_text='You applied to this job!')
        messages.success(request, 'New application added')
        return redirect('dashboard')

    else:
        return render(request, 'applications/application-add.html')

@login_required
def edit(request, application_id):
    application_to_edit = get_object_or_404(Application, pk=application_id, user=request.user)

    context = {
        'application': application_to_edit
    }

    if request.method == 'POST':
        new_values = get_form_data(request)
        updated_application = Application(pk=application_id, **new_values)
        updated_application.save()
        messages.success(request, 'Application updated')
        return redirect('applications')

    else:
        return render(request, 'applications/application-edit.html', context)
    

@login_required
def delete(request, application_id):
    application_to_delete = get_object_or_404(Application, pk=application_id, user=request.user)

    if request.method == 'POST':
        application_to_delete.delete()
        messages.warning(request, 'Application removed')
        return redirect('applications')

    else:
        return redirect('applications')
        
