from django.shortcuts import render
from .models import Event
from django.core.paginator import Paginator

def event_list(request):

    # 1. Retrieve all events
    events = Event.objects.all()

    # 2. Apply pagination (5 events per page)
    paginator = Paginator(events, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 3. Send events to template
    return render(request, 'events/event_list.html', {'page_obj': page_obj})