from django.db import models
from django.conf import settings


class Quiz(models.Model):
    DIFFICULTY_CHOICES = [('easy', 'Лёгкий'), ('medium', 'Средний'), ('hard', 'Сложный')]
    CATEGORY_CHOICES = [
        ('history', 'История'),
        ('symbols', 'Символика'),
        ('personalities', 'Личности'),
        ('general', 'Общие знания'),
    ]
    title = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    time_limit = models.PositiveIntegerField(default=0, help_text='Время в секундах, 0 = без ограничений')
    image = models.ImageField(upload_to='quizzes/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def question_count(self):
        return self.questions.count()


class Question(models.Model):
    TYPE_CHOICES = [
        ('single', 'Один ответ'),
        ('multiple', 'Несколько ответов'),
        ('truefalse', 'Правда / Ложь'),
    ]
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(verbose_name='Вопрос')
    question_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='single')
    image = models.ImageField(upload_to='quizzes/questions/', blank=True, null=True)
    explanation = models.TextField(blank=True, verbose_name='Объяснение')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['order']

    def __str__(self):
        return self.text[:80]


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=500, verbose_name='Ответ')
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.text


class QuizResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quiz_results')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='results')
    score = models.PositiveIntegerField(default=0)
    total_questions = models.PositiveIntegerField(default=0)
    time_taken = models.PositiveIntegerField(default=0, help_text='Секунды')
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Результат теста'
        verbose_name_plural = 'Результаты тестов'
        ordering = ['-completed_at']

    def __str__(self):
        return f'{self.user} — {self.quiz}: {self.score}/{self.total_questions}'

    @property
    def percentage(self):
        if self.total_questions == 0:
            return 0
        return round(self.score / self.total_questions * 100)
