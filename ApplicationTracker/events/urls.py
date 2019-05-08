from django.urls import path

from . import views

urlpatterns = [
    path('add', views.add, name='event-add'),
    path('<int:event_id>/edit', views.edit, name='event-edit'),
    path('<int:event_id>/delete', views.delete, name='event-delete'),
]
