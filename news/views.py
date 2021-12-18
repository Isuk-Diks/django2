from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import OuterRef, Subquery
from django.db import models
from .models import Article, Mention, Project


def blog_handler(request):
    articles = Article.objects.all()[:7]
    context = {"top_article":articles[0], "articles":articles[1:]}
    return render(request, 'news/blog.html', context)


def detail_post(request, slug):
    next_article = Article.objects.filter(created__gte=OuterRef('created')).exclude(id=OuterRef('id'))[:1]
    previous_article = Article.objects.filter(created__lte=OuterRef('created')).exclude(id=OuterRef('id'))[:1]
    article = get_object_or_404(Article.objects.prefetch_related('comments').annotate(
            next_article=Subquery(next_article.values("title")[:1]),
            next_article_slug=Subquery(next_article.values("slug")[:1]),
            previous_article=Subquery(previous_article.values("title")[:1]),
            previous_article_slug=Subquery(previous_article.values("slug")[:1]),),
            slug=slug)
    context = {
            'article':article}
    return render(request, 'news/blog-single.html', context)


def index(request):
    articles = Article.objects.all()[:6]
    mentions = Mention.objects.all()
    projects = Project.objects.all()[:8]
    context = {"articles":articles, "mentions":mentions, "projects":projects}
    return render(request, 'news/index.html', context)
