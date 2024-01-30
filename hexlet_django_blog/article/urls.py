from django.urls import path

from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.ArticleView.as_view()),
    path('<str:tags>/<int:article_id>/', views.article, name='artilce_with_tags_id')
]
