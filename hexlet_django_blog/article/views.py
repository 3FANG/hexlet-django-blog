from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class ArticleView(View):
    def get(self, request, *args, **kwargs) -> HttpResponse:
        return render(request, 'articles/index.html', context={'application': 'hexlet_django_blog.article'})
