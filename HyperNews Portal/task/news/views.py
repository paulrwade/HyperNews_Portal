from django.views import generic
from .models import News
# from datetime import timezone
# from os import link
# from django.shortcuts import render
# import json


class IndexView(generic.ListView):

	template_name = 'news/index.html'
	context_object_name = 'news'
	queryset = News.objects.all()

	def get_queryset(self):
		return self.queryset


class NewsItemListView(generic.ListView):

	template_name = 'news/news_item_list.html'
	context_object_name = 'news_list'
	queryset = News.objects.all()

	def get_queryset(self):
		return self.queryset


class NewsItemDetailView(generic.ListView):
	template_name = 'news/news_item_details.html'
	context_object_name = 'news_item'
	queryset = News.objects.all()

	def get_queryset(self):

		link = self.kwargs.get('link')

		return self.queryset.filter(link=link)

# def index(request):
#     news = News.objects.all()
#     context = {'news': news}
#     return render(request, 'news/news_item_list.html.html', context)
#
#
# def news_item_list.html(request):
#     news = News.objects.all()
#     context = {'news': news}
#     return render(request, 'news/news_item_list.html.html', context)
#
#
# def article_detail(request, link):
#     news = News.objects.filter(link=link)
#     context = {'news': news}
#     return render(request, 'news/news_item_details.html', context)
#
#
# class IndexView(generic.ListView):
#
#     template_name = 'news/news_item_list.html.html'
#
#     def get_queryset(self):
#         return render(self.request, self.template_name)
#
#
# class ArticleDetailView(generic.ListView):
#
#     model = News
#
#     template_name = 'news/news_item_details.html'
#
#     context = {'title': 'title text here',
#                'text': 'article text here',
#                'created_at': 'Date Text Here'}
#
#     def get_queryset(self):
#
#         return render(self.request, self.template_name, self.context)
#
#         # pk = int(self.kwargs.get('pk'))
        #
        # with (open("news/news.json", "r") as json_file):
        #     news_dict_from_json = json.load(json_file)
        #
        #     for this_article in news_dict_from_json:
        #
        #         if int(this_article['link']) == pk:
        #
        #             # context = {'title': this_article["title"],
        #             #            "text": this_article["text"],
        #             #            "created_at": this_article["created_at"]}
        #
        #             context = {'title': 'title text here',
        #                        'text': 'article text here',
        #                        'created_at': 'Date Text Here'}
        #
        #             return render(self.request, self.template_name, context)
