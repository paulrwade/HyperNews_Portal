from django.views import generic
# from django.conf import settings
from .models import News
# import json


class IndexView(generic.ListView):
	template_name = 'news/index.html'

	def get_queryset(self):
		return None


# ------------------------------------------------------
class NewsItemListView(generic.ListView):
	template_name = 'news/news_item_list.html'
	context_object_name = 'news_item_list'

	def get_queryset(self, *args, **kwargs):
		return News.objects.all().order_by('created')


# -----------------------------------------------------
class NewsItemDetailView(generic.ListView):
	template_name = 'news/news_item_details.html'
	context_object_name = 'news_item'

	def get_queryset(self, *args, **kwargs):
		link = self.kwargs.get('link')
		return News.objects.get(link=link).order_by('title')
