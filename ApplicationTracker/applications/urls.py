from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='applications'),
    path('add', views.add, name='application-add'),
    path('<int:application_id>', views.detail, name='detail'),
    path('<int:application_id>/edit', views.edit, name='application-edit'),
    path('<int:application_id>/delete', views.delete, name='application-delete'),
    path('<int:application_id>/event/', include('events.urls')),

]
