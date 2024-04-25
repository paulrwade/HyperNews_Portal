from django.urls import path, include
from views import IndexView, ArticleView


urlpatterns = [
	path("", IndexView.as_view(), name="index"),
	path("news/<int:link>/", ArticleView.as_view(), name="article_details"),
]
