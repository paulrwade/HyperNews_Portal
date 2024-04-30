from django.forms import Form
from django.views import generic
from django.conf import settings
from datetime import datetime
import json


class IndexView(generic.ListView):
	template_name = 'index.html'

	def get_queryset(self):
		return None


# ------------------------------------------------------
class NewsItemListView(generic.ListView):
	template_name = 'news_item_list.html'
	context_object_name = 'news_item_list'

	def get_queryset(self, *args, **kwargs):
		with (open(settings.NEWS_JSON_PATH) as json_file):
			news_item_list = sorted(json.load(json_file), key=lambda k: k['created'])
			for news_item in news_item_list:
				news_item['created'] = datetime.fromisoformat(news_item['created'])
		return news_item_list


# -----------------------------------------------------
class NewsItemDetailView(generic.ListView):
	template_name = 'news_item_details.html'
	context_object_name = 'news_item'

	def get_queryset(self, *args, **kwargs):
		link = self.kwargs.get('link')
		with open(settings.NEWS_JSON_PATH) as json_file:
			my_news = json.load(json_file)
			for news_item in my_news:
				if news_item['link'] == link:
					return news_item


class NewsItemCreateView(generic.CreateView):

	template_name = 'news_item_create.html'
	context_object_name = 'news_item'

	def get_queryset(self):
		return None

	def post(self, request, *args, **kwargs):

		with open(settings.NEWS_JSON_PATH) as json_file:
			my_news = json.load(json_file)

			title = Form.cleaned_data['title']
			text = Form.cleaned_data['text']
			created = str(datetime.now())

			news_item = [{'title': title, 'text': text, 'created': created}]

		if not my_news.contains(news_item):
			my_news.append(news_item)
