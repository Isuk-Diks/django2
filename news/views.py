from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import OuterRef, Subquery
from django.db import models
from .models import Article, Mention, Project
from .forms.comment import CommentForm

def blog_handler(request, page=1):
    per_page = 7
    all_articles = Article.objects.all()
    articles = all_articles[(page-1)*per_page:page*per_page]
    context = {"top_article":articles[0], 
                "articles":articles[1:], 
                "next_page":page+1 if page*per_page<len(all_articles) else None,
                "previous_page":page-1 if page>1 else None}
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
    form = CommentForm()
    
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect("news:detail_post", slug=slug)

    context = {'form':form, 'article':article}
    return render(request, 'news/blog-single.html', context)


def index(request):
    articles = Article.objects.all()[:6]
    mentions = Mention.objects.all()
    projects = Project.objects.all()[:8]
    context = {"articles":articles, "mentions":mentions, "projects":projects}
    return render(request, 'news/index.html', context)
