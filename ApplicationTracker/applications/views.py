from django.shortcuts import render

def index(request):
    return render(request, 'applications/application-list.html')

def detail(request):
    return render(request, 'applications/application-detail.html')