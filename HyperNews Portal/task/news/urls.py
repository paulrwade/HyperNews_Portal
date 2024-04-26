from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:link>/', views.ArticleDetailView.as_view(), name='article_detail'),
]
