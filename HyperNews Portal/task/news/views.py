from django.shortcuts import render
from django.views import generic
from .models import News
from django.conf import settings
import json


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.all()


def article(request, link):

    # ...
    list_item = News.objects.get(link=link)

    if list_item['link'] == link:
        return render(request, 'list_item_page.html', list_item)