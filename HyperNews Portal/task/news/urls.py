from django.urls import path
from . import views
from django.shortcuts import redirect


urlpatterns = [
	path('',lambda req: redirect('news/') ),
	path('news/<int:link>/', views.NewsItemDetailView.as_view(), name='news_item'),
	path('news/', views.NewsItemListView.as_view(), name='news_item_list'),
	path('news/create/', views.NewsItemCreateView.as_view(), name='news_item_create'),
]
