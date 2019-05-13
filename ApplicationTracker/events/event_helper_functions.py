from applications.models import Application
from django.shortcuts import get_object_or_404
from .models import Event
import datetime

def validate_event_type(post_request):
    if post_request.POST['event_type'] in ['Application Submitted', 'Phone Screen', 'Technical Interview', 'On Site Interview', 'Job Offer', 'Note']:
        return True
    else:
        return False

def build_application_with_status(request, application_id, events):
    parent_application = get_object_or_404(Application, pk=application_id, user=request.user)
    for item in ['Job Offer', 'On Site Interview', 'Technical Interview', 'Phone Screen', 'Application Submitted']:
        for event in events:
            status = event.event_type
            if status == item:
                parent_application.status = status
                return parent_application
    return parent_application

def update_application_status(request, application_id):
    events = Event.objects.filter(application=Application.objects.get(pk=application_id))
    application_status = build_application_with_status(request, application_id, events)
    application_status.last_updated = datetime.datetime.now()
    application_status.save()
    return
