from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event
from applications.models import Application

def validate_event_type(post_request):
    if post_request.POST['event_type'] in ['Application Submitted', 'Phone Screen', 'Technical Interview', 'On Site Interview', 'Job Offer', 'Note']:
        return True
    else:
        return False

def get_form_data(post_request, application_id):
    event_fields = ['event_type', 'event_text', 'event_date']
    form_data = {'application': Application.objects.get(pk=application_id)}
    for field in event_fields:
        try:
            if post_request.POST[field] != "":
                form_data[field] = post_request.POST[field]
        except:
            pass
    return form_data


@login_required
def add(request, application_id):
    if request.method == 'POST' and validate_event_type(request) == True:
        event_data = get_form_data(request, application_id)
        new_event = Event.objects.create(**event_data)
        messages.success(request, 'New event added')
        return redirect('detail', application_id)

    else:
        context = {
            'application_id': application_id
        }
        return render(request, 'events/event-add.html', context)

@login_required
def edit(request, event_id, application_id):
    event_to_edit = get_object_or_404(Event, pk=event_id)
    parent_application = get_object_or_404(Application, pk=application_id, user=request.user)

    context = {
        'event': event_to_edit,
        'application': parent_application
    }

    if request.method == 'POST' and validate_event_type(request) == True:
        new_values = get_form_data(request, application_id)
        updated_event = Event(pk=event_id, **new_values)
        updated_event.save()
        messages.success(request, 'Event updated')
        return redirect('detail', application_id)

    else:
        return render(request, 'events/event-edit.html', context)
    

@login_required
def delete(request, event_id, application_id):
    parent_application = get_object_or_404(Application, pk=application_id, user=request.user)
    event_to_delete = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        event_to_delete.delete()
        messages.warning(request, 'Event removed')
        return redirect('detail', application_id)

    else:
        return redirect('detail', application_id)
        
