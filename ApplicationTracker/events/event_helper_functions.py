from applications.models import Application
from .models import Event

def validate_event_type(post_request):
    if post_request.POST['event_type'] in ['Application Submitted', 'Phone Screen', 'Technical Interview', 'On Site Interview', 'Job Offer', 'Note']:
        return True
    else:
        return False

def build_application_with_status(request, application_id, events):
    for item in ['Job Offer', 'On Site Interview', 'Technical Interview', 'Phone Screen', 'Application Submitted']:
        for event in events:
            status = event.event_type
            if status == item:
                application_status = Application(pk=application_id, user=request.user, status=status)
                return application_status

def update_application_status(request, application_id):
        events = Event.objects.filter(application=Application.objects.get(pk=application_id))
        new_application_status = build_application_with_status(request, application_id, events)
        new_application_status.save()
        return
