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


class ArticleFormEditView(View):
    """Представление формы для изменения статьи."""

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        # article = get_object_or_404(Article, article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', context={
            'form': form, 'article_id':article_id
        })

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles_index')

        return render(request, 'articles/update.html', context={
            'form': form, 'article_id':article_id
        })


class ArticleFormDeleteView(View):
    """Представление формы для удаления статьи."""

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles_index')
