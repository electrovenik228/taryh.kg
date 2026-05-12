from django.urls import path
from . import views

app_name = 'history'

urlpatterns = [
    path('', views.period_list, name='list'),
    path('timeline/', views.timeline, name='timeline'),
    path('<slug:slug>/', views.period_detail, name='detail'),
]
