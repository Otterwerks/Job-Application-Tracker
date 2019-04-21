from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('applications', views.applications, name='applications'),
    path('detail', views.detail, name='detail'),

]