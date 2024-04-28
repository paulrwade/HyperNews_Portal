from django.views import generic
from django.conf import settings
# from .models import News
import json


class IndexView(generic.ListView):
	template_name = 'news/index.html'

	def get_queryset(self):
		return None


# ------------------------------------------------------
class NewsItemListView(generic.ListView):
	template_name = 'news/news_item_list.html'
	context_object_name = 'news_item_list'

	def get_queryset(self, *args, **kwargs):
		with open(settings.NEWS_JSON_PATH) as json_file:
			news_item_list = json.load(json_file)
		return news_item_list
		# return News.objects.all().order_by('created')


# -----------------------------------------------------
class NewsItemDetailView(generic.ListView):
	template_name = 'news/news_item_details.html'
	context_object_name = 'news_item'

	def get_queryset(self, *args, **kwargs):
		link = self.kwargs.get('link')
		with open(settings.NEWS_JSON_PATH) as json_file:
			my_news = json.load(json_file)
			my_news = my_news[link]
			return my_news
