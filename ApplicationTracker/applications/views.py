from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .models import Application
from events.models import Event

def get_form_data(post_request):
    application_fields = ['position', 'company', 'location', 'department', 'company_url', 'posting_url', 'portal_url', 'portal_login', 'portal_pass', 'posted_on', 'closes_on', 'applied_on', 'resume', 'cover_letter', 'body']
    form_data = {'user': post_request.user}
    for field in application_fields:
        try:
            if post_request.POST[field] != "":
                form_data[field] = post_request.POST[field]
        except:
            pass
    return form_data


@login_required
def index(request):
    applications = Application.objects.filter(user=request.user)

    context = {
        'applications': applications
    }

    return render(request, 'applications/application-list.html', context)

@login_required
def detail(request, application_id):
    application = get_object_or_404(Application, pk=application_id, user=request.user)
    events = Event.objects.filter(application=application)

    context = {
        'application': application,
        'events': events
    }

    return render(request, 'applications/application-detail.html', context)

@login_required
def add(request):
    if request.method == 'POST':
        application_data = get_form_data(request)
        new_application = Application.objects.create(**application_data)
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
        return redirect('applications')

    else:
        return redirect('applications')
        
