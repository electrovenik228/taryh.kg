from django.urls import path
from . import views

app_name = 'symbols'

urlpatterns = [
    path('', views.symbols_home, name='home'),
    path('flag/', views.flag, name='flag'),
    path('emblem/', views.emblem, name='emblem'),
    path('anthem/', views.anthem, name='anthem'),
]
