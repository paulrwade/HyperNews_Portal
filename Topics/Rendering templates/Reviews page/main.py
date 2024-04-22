from django.shortcuts import render
from django.views import View


class ReviewView(View):

	reviews = ['Neato!', 'That book was supercalifragilisticexpialidocious', 'It was a ok, I guess']

	context = {'reviews': reviews}

	def get(self, request):

		return render(request, 'book/reviews.html', context={"reviews": self.reviews})
