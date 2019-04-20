from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def applications(request):
    return render(request, 'pages/application-list.html')