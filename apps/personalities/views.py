from django.shortcuts import render, get_object_or_404
from .models import Personality
from apps.history.models import HistoricalPeriod


def personality_list(request):
    period_slug = request.GET.get('period', '')
    personalities = Personality.objects.select_related('period').all()
    if period_slug:
        personalities = personalities.filter(period__slug=period_slug)
    periods = HistoricalPeriod.objects.all()
    return render(request, 'personalities/list.html', {
        'personalities': personalities,
        'periods': periods,
        'selected_period': period_slug,
    })


def personality_detail(request, slug):
    person = get_object_or_404(Personality, slug=slug)
    related = Personality.objects.filter(period=person.period).exclude(slug=slug)[:3]
    return render(request, 'personalities/detail.html', {
        'person': person,
        'related': related,
    })
