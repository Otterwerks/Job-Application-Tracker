from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='applications'),
    path('add', views.add, name='add'),
    path('<int:application_id>', views.detail, name='detail'),
]