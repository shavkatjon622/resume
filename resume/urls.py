from django.urls import path

from config import settings
from .views import index
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)