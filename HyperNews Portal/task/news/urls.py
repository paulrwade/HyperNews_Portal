from django.urls import path
from . import views


urlpatterns = [
	path('', views.IndexView.as_view(), name='coming_soon.html'),
	path('news/', views.NewsItemListView.as_view(), name='news_item_list'),
	path('news/<int:link>/', views.NewsItemDetailView.as_view(), name='news_item'),
	path('news/create/', views.NewsItemCreateView.as_view(), name='news_item_create'),
]
