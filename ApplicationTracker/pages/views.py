from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'pages/index.html')

def features(request):
    return render(request, 'pages/features.html')

def events(request):
    return render(request, 'pages/events.html')

def visuals(request):
    return render(request, 'pages/visualization.html')

