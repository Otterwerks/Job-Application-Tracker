from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('features', views.features, name='features'),
    path('features/events', views.events, name='events'),
    path('features/visuals', views.visuals, name='visuals'),

]