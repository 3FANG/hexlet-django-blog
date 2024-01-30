from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect


class HomePageView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['who'] = "World"
        return

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return redirect(reverse("artilce_with_tags_id", kwargs={'tags': 'python', 'article_id': 42}))


def about(request):
    return render(request, 'about.html')
