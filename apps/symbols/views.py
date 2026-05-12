from django.shortcuts import render, get_object_or_404
from .models import Symbol, AnthemVerse


def symbols_home(request):
    symbols = {s.symbol_type: s for s in Symbol.objects.prefetch_related('elements').all()}
    return render(request, 'symbols/home.html', {'symbols': symbols})


def flag(request):
    symbol = Symbol.objects.filter(symbol_type='flag').prefetch_related('elements').first()
    elements = symbol.elements.all() if symbol else []
    return render(request, 'symbols/flag.html', {'symbol': symbol, 'elements': elements})


def emblem(request):
    symbol = Symbol.objects.filter(symbol_type='emblem').prefetch_related('elements').first()
    elements = symbol.elements.all() if symbol else []
    return render(request, 'symbols/emblem.html', {'symbol': symbol, 'elements': elements})


def anthem(request):
    symbol = Symbol.objects.filter(symbol_type='anthem').first()
    verses = AnthemVerse.objects.all()
    return render(request, 'symbols/anthem.html', {'symbol': symbol, 'verses': verses})
