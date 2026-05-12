from django.db import models


class Symbol(models.Model):
    TYPE_CHOICES = [
        ('flag', 'Флаг'),
        ('emblem', 'Герб'),
        ('anthem', 'Гимн'),
    ]
    symbol_type = models.CharField(max_length=10, choices=TYPE_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    history = models.TextField(blank=True, verbose_name='История создания')
    image = models.ImageField(upload_to='symbols/', blank=True, null=True)
    audio = models.FileField(upload_to='symbols/audio/', blank=True, null=True)

    class Meta:
        verbose_name = 'Государственный символ'
        verbose_name_plural = 'Государственные символы'

    def __str__(self):
        return self.title


class SymbolElement(models.Model):
    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE, related_name='elements')
    name = models.CharField(max_length=200, verbose_name='Элемент')
    description = models.TextField(verbose_name='Описание')
    meaning = models.TextField(blank=True, verbose_name='Значение')
    # SVG coordinates for interactive hotspot (percentage-based)
    x_percent = models.FloatField(default=50, help_text='X позиция в % от ширины')
    y_percent = models.FloatField(default=50, help_text='Y позиция в % от высоты')

    class Meta:
        verbose_name = 'Элемент символа'
        verbose_name_plural = 'Элементы символа'

    def __str__(self):
        return f'{self.symbol} — {self.name}'


class AnthemVerse(models.Model):
    order = models.PositiveIntegerField()
    verse_type = models.CharField(max_length=10, choices=[('verse', 'Куплет'), ('chorus', 'Припев')])
    text_ky = models.TextField(verbose_name='Текст (кыргызский)')
    text_ru = models.TextField(blank=True, verbose_name='Текст (русский)')

    class Meta:
        verbose_name = 'Строфа гимна'
        verbose_name_plural = 'Строфы гимна'
        ordering = ['order']

    def __str__(self):
        return f'{"Куплет" if self.verse_type == "verse" else "Припев"} {self.order}'
