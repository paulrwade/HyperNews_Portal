from django.urls import path, include
from . import views


urlpatterns = [
	path('news/<int:link>/', views.NewsItemDetailView.as_view(), name='news_item'),
	path('', views.NewsItemListView.as_view(), name='news_item_list'),
]
