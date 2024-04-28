from django.views import generic
from django.conf import settings
# from .models import News
import json


class IndexView(generic.ListView):
	template_name = settings.NEWS_TEMPLATE_PATH + 'index.html'

	def get_queryset(self):
		return None


# ------------------------------------------------------
class NewsItemListView(generic.ListView):
	template_name = settings.NEWS_TEMPLATE_PATH + 'news_item_list.html'
	context_object_name = 'news_item_list'

	def get_queryset(self, *args, **kwargs):
		my_news = json.loads(settings.NEWS_ITEM_LIST + 'news.json')
		return my_news.order_by('created')
		# return News.objects.all().order_by('created')


# -----------------------------------------------------
class NewsItemDetailView(generic.ListView):
	template_name = settings.NEWS_TEMPLATE_PATH + 'news_item_details.html'
	context_object_name = 'news_item'

	def get_queryset(self, *args, **kwargs):
		my_news = json.loads(settings.NEWS_ITEM_LIST + 'news.json')
		link = self.kwargs.get('link')
		if link:
			my_news = my_news[link]
			return my_news.order_by('created')
			# return News.objects.get(link=link).order_by('title')
