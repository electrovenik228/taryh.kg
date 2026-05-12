from django.shortcuts import render
from apps.history.models import HistoricalPeriod, HistoricalEvent
from apps.personalities.models import Personality
from apps.quizzes.models import Quiz
from apps.symbols.models import Symbol
from .models import SiteStat


def home(request):
    periods = HistoricalPeriod.objects.all()
    symbols = Symbol.objects.all()
    featured_quizzes = Quiz.objects.filter(is_active=True)[:3]
    featured_personalities = Personality.objects.filter(is_featured=True)[:4]
    recent_events = HistoricalEvent.objects.filter(is_featured=True).order_by('-year')[:5]
    stats = SiteStat.objects.all()
    return render(request, 'core/home.html', {
        'periods': periods,
        'symbols': symbols,
        'featured_quizzes': featured_quizzes,
        'featured_personalities': featured_personalities,
        'recent_events': recent_events,
        'stats': stats,
    })
