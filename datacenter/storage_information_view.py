from datacenter.models import Passcard, format_duration
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visit = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []

    for v in visit:
        non_closed_visits.append(
            {
                'who_entered': v.passcard.owner_name,
                'entered_at': v.entered_at,
                'duration': format_duration(v.get_duration())
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
