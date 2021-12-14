from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Article, Mention, Project

def blog_handler(request):
    articles = Article.objects.all()[:7]
    context = {"top_article":articles[0], "articles":articles[1:]}
    return render(request, 'news/blog.html', context)


def detail_post(request, slug):
    article = get_object_or_404(Article.objects.prefetch_related('comments'), slug=slug)
    context = {'article':article}
    return render(request, 'news/blog-single.html', context)


def index(request):
    articles = Article.objects.all()[:6]
    mentions = Mention.objects.all()
    projects = Project.objects.all()[:8]
    context = {"articles":articles, "mentions":mentions, "projects":projects}
    return render(request, 'news/index.html', context)
