from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.duration import get_duration, format_duration


def storage_information_view(request):
    active_visits_queryset = Visit.objects.filter(leaved_at=None)
    active_visits = []

    for visit in active_visits_queryset:
        local_entered_at = localtime(visit.entered_at)
        visit_duration = get_duration(visit)
        formatted_duration = format_duration(visit_duration)
        visitor_name = visit.passcard.owner_name

        visit.visitor_name = visitor_name
        visit.local_entered_at = local_entered_at
        visit.visit_duration = formatted_duration

        active_visits.append(visit)
    
    context = {
        'active_visits': active_visits,
    }
    
    return render(request, 'storage_information.html', context)