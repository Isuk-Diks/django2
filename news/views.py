from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import OuterRef, Subquery, Prefetch
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from .models import Article, Mention, Project, Comment
from .forms.comment import CommentForm


class BlogListView(ListView):
    template_name = 'news/blog.html'
    model = Article
    ordering = '-created'
    paginate_by = 7

class ArticleDetailView(DetailView, FormView):
    model = Article
    form_class = CommentForm
    template_name = 'news/blog-single.html'
    def get_success_url(self):
        return reverse('news:detail_post', kwargs={'slug': self.object.slug})

    def get_object(self):
        next_article = Article.objects.filter(created__gte=OuterRef('created')).exclude(id=OuterRef('id'))[:1]
        previous_article = Article.objects.filter(created__lte=OuterRef('created')).exclude(id=OuterRef('id'))[:1]
        article = get_object_or_404(Article.objects.prefetch_related(
            Prefetch('comments', Comment.objects.filter(is_moderated=True))).annotate(
            next_article=Subquery(next_article.values("title")[:1]),
            next_article_slug=Subquery(next_article.values("slug")[:1]),
            previous_article=Subquery(previous_article.values("title")[:1]),
            previous_article_slug=Subquery(previous_article.values("slug")[:1]),),
            slug=self.kwargs['slug'])
        return article


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)


class IndexView(TemplateView):
    template_name = "news/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.all()[:6]
        mentions = Mention.objects.all()
        projects = Project.objects.all()[:8]
        context = {"articles":articles, "mentions":mentions, "projects":projects}
        return context
