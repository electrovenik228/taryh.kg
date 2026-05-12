from django.db import models


class HistoricalPeriod(models.Model):
    PERIOD_CHOICES = [
        ('ancient', 'Древний Кыргызстан'),
        ('khaganate', 'Кыргызский каганат'),
        ('manas', 'Эпоха Манаса'),
        ('khanate', 'Кокандское ханство'),
        ('empire', 'Российская империя'),
        ('ussr', 'Советский период'),
        ('independent', 'Независимый Кыргызстан'),
    ]
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200, verbose_name='Название')
    period_type = models.CharField(max_length=20, choices=PERIOD_CHOICES, unique=True)
    description = models.TextField(verbose_name='Описание')
    short_description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='history/periods/', blank=True, null=True)
    start_year = models.IntegerField(verbose_name='Начало (год)')
    end_year = models.IntegerField(null=True, blank=True, verbose_name='Конец (год)')
    order = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=7, default='#E8112D', help_text='HEX цвет для карточки')

    class Meta:
        verbose_name = 'Исторический период'
        verbose_name_plural = 'Исторические периоды'
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_year_range(self):
        if self.end_year:
            return f'{self.start_year} – {self.end_year}'
        return f'{self.start_year} – настоящее время'


class HistoricalEvent(models.Model):
    period = models.ForeignKey(HistoricalPeriod, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=300, verbose_name='Событие')
    description = models.TextField(verbose_name='Описание')
    year = models.IntegerField(verbose_name='Год')
    month = models.IntegerField(null=True, blank=True, verbose_name='Месяц')
    day = models.IntegerField(null=True, blank=True, verbose_name='День')
    image = models.ImageField(upload_to='history/events/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Историческое событие'
        verbose_name_plural = 'Исторические события'
        ordering = ['year', 'month', 'day']

    def __str__(self):
        return f'{self.year}: {self.title}'
