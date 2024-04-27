from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('news/', views.IndexView.as_view(), name='index'),
	path('news-items-list/', views.NewsItemListView.as_view(), name='news_item_list'),
	path('news-item/<int:link>/', views.NewsItemDetailView.as_view(), name='news_item'),
]
