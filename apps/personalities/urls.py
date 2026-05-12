from django.urls import path
from . import views

app_name = 'personalities'

urlpatterns = [
    path('', views.personality_list, name='list'),
    path('<slug:slug>/', views.personality_detail, name='detail'),
]
