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
        return context

    # def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     return redirect(reverse("article_id", kwargs={'id': 1}))


def about(request):
    return render(request, 'about.html')
