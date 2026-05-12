from django.contrib import admin
from .models import Symbol, SymbolElement, AnthemVerse


class ElementInline(admin.TabularInline):
    model = SymbolElement
    extra = 1


@admin.register(Symbol)
class SymbolAdmin(admin.ModelAdmin):
    list_display = ('title', 'symbol_type')
    inlines = [ElementInline]


@admin.register(AnthemVerse)
class AnthemVerseAdmin(admin.ModelAdmin):
    list_display = ('order', 'verse_type')
    list_editable = ('verse_type',)
    ordering = ('order',)
