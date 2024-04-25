import requests
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


class ArticleView(generic.ListView):

    template_name = 'news/article_details.html'

    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.all()
