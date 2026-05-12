from django.db import models


class SiteStat(models.Model):
    """Stores platform-wide statistics shown on the home page."""
    label = models.CharField(max_length=100)
    value = models.PositiveIntegerField(default=0)
    icon = models.CharField(max_length=50, blank=True, help_text='Heroicon name')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'
        ordering = ['order']

    def __str__(self):
        return f'{self.label}: {self.value}'
