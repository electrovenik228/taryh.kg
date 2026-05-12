from django.shortcuts import render, get_object_or_404
from .models import HistoricalPeriod, HistoricalEvent


def period_list(request):
    periods = HistoricalPeriod.objects.prefetch_related('events').all()
    all_events = HistoricalEvent.objects.select_related('period').order_by('year')
    return render(request, 'history/period_list.html', {
        'periods': periods,
        'all_events': all_events,
    })


def period_detail(request, slug):
    period = get_object_or_404(HistoricalPeriod, slug=slug)
    events = period.events.order_by('year')
    other_periods = HistoricalPeriod.objects.exclude(slug=slug)
    return render(request, 'history/period_detail.html', {
        'period': period,
        'events': events,
        'other_periods': other_periods,
    })


def timeline(request):
    events = HistoricalEvent.objects.select_related('period').order_by('year')
    periods = HistoricalPeriod.objects.all()
    selected_period = request.GET.get('period', 'all')
    if selected_period != 'all':
        events = events.filter(period__slug=selected_period)
    return render(request, 'history/timeline.html', {
        'events': events,
        'periods': periods,
        'selected_period': selected_period,
    })
