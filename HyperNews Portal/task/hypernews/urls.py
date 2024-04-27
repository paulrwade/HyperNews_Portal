from django.contrib import admin
from django.contrib.admindocs import views
from django.urls import path, include


urlpatterns = [
    path('', include('news.urls')),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
]
