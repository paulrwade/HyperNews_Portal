from django.views import generic
from django.shortcuts import render
from .models import News


class IndexView(generic.ListView):
	template_name = 'news/index.html'

	def get_queryset(self):
		return None


class NewsItemListView(generic.ListView):

	model = News
	template_name = 'news/news_item_list.html'

	def get_queryset(self):
		return News.objects.all()


class NewsItemDetailView(generic.ListView):
	template_name = 'news/news_item_details.html'
	context_object_name = 'news_item'

	def get_context_data(self, **kwargs):
		link = self.kwargs.get('link')
		context = News.objects.all().filter(link=link)
		return context

# class IndexView(generic.ListView):
#
#     template_name = 'news/news_item_list_old.html.html'
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
