from django.views import generic
from django.shortcuts import render
from .models import News
import json


class IndexView(generic.ListView):

    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.all()


class ArticleDetailView(generic.ListView):

    model = News
    template_name = 'news/article_details.html'

    def get_queryset(self, *args, **kwargs):

        link = self.kwargs.get('pk')

        with (open("news/news.json", "r") as json_file):

            news_dict_from_json = json.load(json_file)

            for this_article in news_dict_from_json:
                if this_article['link'] == link:
                    return render(self.request, template_name='news/article_details.html', context=this_article)
