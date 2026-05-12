from django.contrib import admin
from .models import HistoricalPeriod, HistoricalEvent


class EventInline(admin.TabularInline):
    model = HistoricalEvent
    extra = 1
    fields = ('year', 'title', 'is_featured')


@admin.register(HistoricalPeriod)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('title', 'period_type', 'start_year', 'end_year', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [EventInline]


@admin.register(HistoricalEvent)
class EventAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'period', 'is_featured')
    list_filter = ('period', 'is_featured')
    search_fields = ('title', 'description')
    ordering = ('year',)
