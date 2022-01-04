from django.shortcuts import render
from django.db.models import Q
from news.models import Article


def search(request):
	context = {}
	query = request.GET.get("query", None)
	if query:
		articles = Article.objects.filter(Q(title__contains=query)|Q(text__contains=query))
		context["articles"] = articles
		context["query"] = query
	return render(request, "search/search.html", context)
