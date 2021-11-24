from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('backend.routes')),
    path('news/', include('news.urls')),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
