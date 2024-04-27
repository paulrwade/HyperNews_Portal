from django.views import generic
from django.shortcuts import render
from .models import News


class IndexView(generic.ListView):
	template_name = 'news/index.html'

	def get_queryset(self):
		return None


class NewsItemListView(generic.ListView):
	template_name = 'news/news_item_list.html'
	context_object_name = 'news_item_list'

	def get_queryset(self, *args, **kwargs):
		return News.objects.all()


class NewsItemDetailView(generic.ListView):
	template_name = 'news/news_item_details.html'
	context_object_name = 'news_item'

	def get_queryset(self, *args, **kwargs):
		link = self.kwargs.get('link')
		return News.objects.get(link=link)
