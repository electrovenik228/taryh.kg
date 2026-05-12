from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('users/', include('apps.users.urls')),
    path('history/', include('apps.history.urls')),
    path('symbols/', include('apps.symbols.urls')),
    path('quizzes/', include('apps.quizzes.urls')),
    path('personalities/', include('apps.personalities.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
