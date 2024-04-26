from django.urls import path, include
from .views import IndexView, ArticleDetailView


urlpatterns = [
	path("news/<int:pk>/", ArticleDetailView.as_view(), name="article_details"),
	path("", IndexView.as_view(), name="index"),
]
