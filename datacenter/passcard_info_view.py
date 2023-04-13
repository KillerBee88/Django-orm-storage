from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datacenter.duration import get_duration, format_duration


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    related_visits = Visit.objects.filter(passcard=passcard)
    passcard_visits_info = []

    for visit in related_visits:
        visit_duration = get_duration(visit)
        formatted_duration = format_duration(visit_duration)
        is_strange_visit = visit_duration.total_seconds() > 3600

        passcard_visits_info.append({
            'entered_at': visit.entered_at,
            'duration': formatted_duration,
            'is_strange': is_strange_visit
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': passcard_visits_info
    }
    return render(request, 'passcard_info.html', context)
