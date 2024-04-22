from django.views import generic


class IndexView(generic.ListView):
    template_name = 'news/coming_soon.html'
