from django.contrib import admin
from .models import Personality


@admin.register(Personality)
class PersonalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'period', 'birth_year', 'death_year', 'is_featured')
    list_filter = ('period', 'is_featured')
    search_fields = ('name', 'biography')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_featured',)
