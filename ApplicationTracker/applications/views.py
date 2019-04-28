from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from applications.models import Application
from django.contrib import messages


@login_required
def index(request):
    return render(request, 'applications/application-list.html')

@login_required
def detail(request):
    return render(request, 'applications/application-detail.html')

@login_required
def add(request):
    if request.method == 'POST':
        application_fields = ['position', 'company', 'location', 'department', 'company_url', 'posting_url', 'portal_url', 'portal_login', 'portal_pass', 'posted_on', 'closes_on', 'applied_on', 'resume', 'cover_letter', 'body']
        application_data = {'user': request.user}
        for field in application_fields:
            try:
                application_data[field] = request.POST[field]
            except:
                pass

        new_application = Application.objects.create(application_data)
        messages.success(request, 'New application added')
        return redirect('dashboard')


    else:
        return render(request, 'applications/application-add.html')