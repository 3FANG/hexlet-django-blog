from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs) -> HttpResponse:
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles
        })


def article(request, tags: str, article_id: int) -> HttpResponse:
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")
