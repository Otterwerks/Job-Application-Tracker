from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from pygal.style import DarkGreenBlueStyle
from applications.charts import RecruitmentFunnel

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first']
        last_name = request.POST['last']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Please choose a different username')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already in use')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'Account created, please log in')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have been logged out successfully')
        return redirect('index')
    

def dashboard(request):
    app_chart = RecruitmentFunnel(
        height=600,
        width=1024,
        explicit_size=True,
        show_legend=False,
        include_y_axis=False,
        include_x_axis=False,
        show_y_labels=False,
        style=DarkGreenBlueStyle(label_font_size=14)
    )

    site_chart = RecruitmentFunnel(
        height=600,
        width=1024,
        explicit_size=True,
        show_legend=False,
        include_y_axis=False,
        include_x_axis=False,
        show_y_labels=False,
        style=DarkGreenBlueStyle(label_font_size=14)
    )


    
    context = {
        'app_chart': app_chart.generate(request.user),
        'site_chart': site_chart.generate()
    }

    return render(request, 'accounts/dashboard.html', context)