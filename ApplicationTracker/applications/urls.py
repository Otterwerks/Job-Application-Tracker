from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='applications'),
    path('offer', views.offer, name='sort-offer'),
    path('onsite', views.onsite, name='sort-onsite'),
    path('technical', views.technical, name='sort-technical'),
    path('phonescreen', views.phonescreen, name='sort-phonescreen'),
    path('submitted', views.submitted, name='sort-submitted'),
    path('add', views.add, name='application-add'),
    path('<int:application_id>', views.detail, name='detail'),
    path('<int:application_id>/edit', views.edit, name='application-edit'),
    path('<int:application_id>/delete', views.delete, name='application-delete'),
    path('<int:application_id>/event/', include('events.urls')),

]
