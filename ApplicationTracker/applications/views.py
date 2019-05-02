from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Application
from django.contrib import messages


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

    context = {
        'application': application
    }

    return render(request, 'applications/application-detail.html', context)

@login_required
def add(request):
    if request.method == 'POST':
        application_fields = ['position', 'company', 'location', 'department', 'company_url', 'posting_url', 'portal_url', 'portal_login', 'portal_pass', 'posted_on', 'closes_on', 'applied_on', 'resume', 'cover_letter', 'body']
        application_data = {'user': request.user}
        for field in application_fields:
            try:
                if request.POST[field] != "":
                    application_data[field] = request.POST[field]
            except:
                pass

        new_application = Application.objects.create(**application_data)
        messages.success(request, 'New application added')
        return redirect('dashboard')


    else:
        return render(request, 'applications/application-add.html')

@login_required
def delete(request, application_id):
    application_to_delete = get_object_or_404(Application, pk=application_id, user=request.user)

    if request.method == 'POST':
        application_to_delete.delete()
        return redirect('applications')

    else:
        return redirect('applications')
        
