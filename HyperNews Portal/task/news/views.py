from django.views import generic
from django.shortcuts import render
from .models import News
import json


def index(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'news/article_list.html', context)


def article_list(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'news/article_list.html', context)


def article_detail(request, link):
    news = News.objects.get(link=link)
    context = {'news': news}
    return render(request, 'news/article_details.html', context)


# class IndexView(generic.ListView):
#
#     template_name = 'news/article_list.html'
#
#     def get_queryset(self):
#         return render(self.request, self.template_name)
#
#
# class ArticleDetailView(generic.ListView):
#
#     model = News
#
#     template_name = 'news/article_details.html'
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
