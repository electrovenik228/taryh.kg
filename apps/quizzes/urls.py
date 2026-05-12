from django.urls import path
from . import views

app_name = 'quizzes'

urlpatterns = [
    path('', views.quiz_list, name='list'),
    path('<int:pk>/take/', views.quiz_take, name='take'),
    path('result/<int:pk>/', views.quiz_result, name='result'),
]
