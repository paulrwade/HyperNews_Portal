from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('news/', views.ArticleListView.as_view(), name='articles'),
	path('news/<int:link>/', views.ArticleDetailView.as_view(), name='article'),
]
