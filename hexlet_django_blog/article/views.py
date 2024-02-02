from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from hexlet_django_blog.article.models import Article


class ArticleView(View):
    def get(self, request, *args, **kwargs) -> HttpResponse:
        return render(request, 'articles/index.html', context={'articles': Article.objects.all()})


def article(request, tags: str, article_id: int) -> HttpResponse:
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")
