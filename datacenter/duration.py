from django.utils.timezone import localtime


def get_duration(visit):
    is_active_visit = visit.leaved_at is None

    if is_active_visit:
        visit_leaved_at = localtime()
    else:
        visit_leaved_at = visit.leaved_at

    visit_duration = visit_leaved_at - visit.entered_at

    return visit_duration

def format_duration(duration):
    hours, remainder = divmod(duration.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{hours}ч {minutes}мин"