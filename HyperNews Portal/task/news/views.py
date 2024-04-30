# from django.http import HttpRequest
# from django.shortcuts import render
from .models import News
from .forms import CreateNewsItemForm
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


# ------------------------------------------------------
class NewsItemCreateView(generic.CreateView):
	template_name = 'news_item_create.html'
	model = News
	fields = ['title', 'text']
	success_url = "/news/"

	def post(self, request, *args, **kwargs):

		news_item = CreateNewsItemForm(request.POST)
		form = self.form_class(news_item)

		if form.is_valid():
			with open(settings.NEWS_JSON_PATH) as json_file:

				news_list = json.load(json_file)

				if news_item not in news_list:
					news_list.append(form.cleaned_data)

# --------------------------------------------------------
# class NewsItemUpdateView(generic.UpdateView):
# 	model = News
# 	fields = ['title', 'text', 'created']
#
#
# class NewsItemDeleteView(generic.DeleteView):
# 	model = News
# 	fields = ['title', 'text', 'created']

# 	template_name = 'news_item_create.html'
# 	form_class = CreateNewsItemForm
# 	success_url = "/thanks/"
#
# 	def form_valid(self, form):
# 		return super().form_valid(form)
#
# 	def post(self, request, *args, **kwargs):
#
# 		if request.POST:
#
# 			if self.form.is_valid():
#
# 				title = self.form.cleaned_data.get("title")
# 				text = self.form.cleaned_data.get("text")
#
# 				with open(settings.NEWS_JSON_PATH) as json_file:
# 					my_news = json.load(json_file)
#
# 					news_item = [{'title': title, 'text': text, 'created': str(datetime.now())}]
#
# 					if not my_news.contains(news_item):
# 						my_news.append(news_item)
#
# 		return render(request, template_name=self.template_name, context=self.context)
#
#
# # --------------------------------------------------
