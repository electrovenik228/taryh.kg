import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg, Count
from .models import Quiz, Question, QuizResult


def quiz_list(request):
    category = request.GET.get('category', '')
    difficulty = request.GET.get('difficulty', '')
    quizzes = Quiz.objects.filter(is_active=True).annotate(
        result_count=Count('results'),
        avg_score=Avg('results__score'),
    )
    if category:
        quizzes = quizzes.filter(category=category)
    if difficulty:
        quizzes = quizzes.filter(difficulty=difficulty)
    return render(request, 'quizzes/list.html', {
        'quizzes': quizzes,
        'category': category,
        'difficulty': difficulty,
        'categories': Quiz.CATEGORY_CHOICES,
        'difficulties': Quiz.DIFFICULTY_CHOICES,
    })


@login_required
def quiz_take(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk, is_active=True)
    questions = quiz.questions.prefetch_related('answers').all()
    if not questions:
        messages.warning(request, 'В этом тесте пока нет вопросов.')
        return redirect('quizzes:list')

    if request.method == 'POST':
        score = 0
        total = questions.count()
        for question in questions:
            if question.question_type == 'multiple':
                selected_ids = set(map(int, request.POST.getlist(f'q_{question.id}', [])))
                correct_ids = set(question.answers.filter(is_correct=True).values_list('id', flat=True))
                if selected_ids == correct_ids:
                    score += 1
            else:
                selected_id = request.POST.get(f'q_{question.id}')
                if selected_id and question.answers.filter(id=selected_id, is_correct=True).exists():
                    score += 1

        time_taken = int(request.POST.get('time_taken', 0))
        result = QuizResult.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            total_questions=total,
            time_taken=time_taken,
        )
        return redirect('quizzes:result', pk=result.pk)

    return render(request, 'quizzes/take.html', {
        'quiz': quiz,
        'questions': questions,
    })


@login_required
def quiz_result(request, pk):
    result = get_object_or_404(QuizResult, pk=pk, user=request.user)
    leaderboard = QuizResult.objects.filter(quiz=result.quiz).select_related('user').order_by('-score', 'time_taken')[:10]
    return render(request, 'quizzes/result.html', {
        'result': result,
        'leaderboard': leaderboard,
    })
