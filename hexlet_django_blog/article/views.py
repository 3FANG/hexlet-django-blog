from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleForm


class IndexView(View):
    """Представление для домашней страницы статей (списка статей)."""

    def get(self, request, *args, **kwargs) -> HttpResponse:
        print('yes' if request.GET else 'no')
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles
        })


class ArticleView(View):
    """Представление для конкретной статьи."""

    def get(self, request, *args, **kwargs) -> HttpResponse:
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class ArticleFormCreateView(View):
    """Представление формы для создания новой статьи."""

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles_index')
        return render(request, 'articles/create.html', context={
            'form': form
        })
