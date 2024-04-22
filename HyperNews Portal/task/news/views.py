from django.views import generic
from .models import News


class IndexView(generic.ListView):
    template_name = 'news/coming_soon.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.all()
