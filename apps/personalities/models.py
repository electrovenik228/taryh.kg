from django.db import models


class Personality(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    slug = models.SlugField(unique=True)
    birth_year = models.IntegerField(null=True, blank=True, verbose_name='Год рождения')
    death_year = models.IntegerField(null=True, blank=True, verbose_name='Год смерти')
    period = models.ForeignKey(
        'history.HistoricalPeriod',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='personalities',
        verbose_name='Эпоха',
    )
    photo = models.ImageField(upload_to='personalities/', blank=True, null=True)
    short_bio = models.CharField(max_length=300, verbose_name='Краткая биография')
    biography = models.TextField(verbose_name='Биография')
    role = models.CharField(max_length=200, verbose_name='Историческая роль')
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Историческая личность'
        verbose_name_plural = 'Исторические личности'
        ordering = ['birth_year']

    def __str__(self):
        return self.name

    def get_years(self):
        if self.birth_year and self.death_year:
            return f'{self.birth_year} – {self.death_year}'
        elif self.birth_year:
            return f'{self.birth_year} – ?'
        return ''
