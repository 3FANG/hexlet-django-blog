from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs) -> HttpResponse:
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs) -> HttpResponse:
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })
