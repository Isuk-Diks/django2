from django.shortcuts import render


def blog_handler(request):
    context = {}
    return render(request, 'news/blog.html', context)


def detail_post(request):
    context = {}
    return render(request, 'news/blog-single.html', context)


def index(request):
    context = {}
    return render(request, 'news/index.html', context)
