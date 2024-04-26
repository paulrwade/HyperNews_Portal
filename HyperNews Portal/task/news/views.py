from django.views import generic
from django.shortcuts import render
from .models import News
import json


class IndexView(generic.ListView):

    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.all()


class ArticleView(generic.ListView):

    def get_queryset(self, *args, **kwargs):

        link = self.kwargs.get('link')

        with (open("/Users/paulwade/Documents/GitHub/HyperNews_Portal/HyperNews Portal/task/news/news.json", "r")
              as json_file):

            news_dict_from_json = json.load(json_file)

            for this_article in news_dict_from_json:
                if this_article['link'] == link:
                    return render(self.request, template_name='news/article.html', context={'article': this_article})
