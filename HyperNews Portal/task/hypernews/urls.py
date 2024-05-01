from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', include('news.urls')),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
]
